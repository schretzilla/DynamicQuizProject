var quizDetail = angular.module('quizDetail',[]);

quizDetail.config(function($interpolateProvider){
    //allow django templates and angular to co-exist
	$interpolateProvider.startSymbol('{[{');
	$interpolateProvider.endSymbol('}]}');
});

quizDetail.directive('showChoices', function() {
    return {
        restrict: 'E',
        link: function(scope, element, attrs){
            scope.choices = attrs.question.choice_set.all();
        },
        template: '<p ng-repeat="choice in choices">{{choice.id}}</p> <p>test</p>'
    };
});

quizDetail.controller('QuizDetailCtrl', function QuizDetailCtrl($scope, $log, $http){

    //On page load
    $scope.loadQuestions = function() {
       //save cur quiz id
       $http.get('/dynoquiz/api/quiz/'+$scope.quizId+'/question').then(function(response){
            $scope.questions = response.data;
       });
    };

    $scope.getChoices = function(questionId) {
        $http.get('/dynoquiz/api/question/'+questionId).then(function(response) {
             return response.data;
        });
    };

    //TODO: Load question on edit click
    $scope.getFullQuestion = function(questionId) {
       $http.get('/dynoquiz/api/quiz/'+$scope.quizId+'/question/'+questionId).then(function(response){
            $scope.questions = response.data;
       },
            function(data) {
                //Error
                alert("error: on get full question: " +data );
            });
    };

    $scope.addQuestion = function(){
        question = {
            'quiz':$scope.quizId,
            'question_text':$scope.questionText,
            'date_created':new Date()
        };
        $http.post('/dynoquiz/api/quiz/'+$scope.quizId+'/question/', question).then(function(){
            $scope.loadQuestions();
            $scope.question=null;

        });
    };

    $scope.updateQuestion = function(){
        question = {
            'id':focusedQuestion.id,
            'quiz':focusedQuestion.quiz,
            'question_text':$scope.questionText,
            'date_created':focusedQuestion.date_created
        };

        $http.put('/dynoquiz/api/quiz/'+$scope.quizId+'/question/'+focusedQuestion.id, question).then(function(){
            $scope.loadQuestions();
        }, function(response) {
            alert("error: " + response.data);
        });
    };

    $scope.deleteQuestion = function(questionId) {
        //alert("Deleting question: " + questionId);
        $http.delete('/dynoquiz/api/quiz/'+$scope.quizId+'/question/'+questionId).then(function(){
            $scope.loadQuestions();
        });
    };

    //Set Focused Question when Edit is selected
    setFocusedQuestion = function(question) {
        focusedQuestion = {
            'id':question.id,
            'question_text':question.question_text,
            'quiz':question.quiz,
            'date_created':question.date_created
        };
    };

    loadQuestionFields = function(question) {
        $scope.questionText = question.question_text;
    };

    $scope.formsetEditQuestion = function(question) {
        setFocusedQuestion(question);
        loadQuestionFields(focusedQuestion);
    };

    $scope.loadPage = function(curQuizId) {
        //save persistant variables
        $scope.quizId = curQuizId;
        $scope.loadQuestions();
        //$scope.getFullQuestion(1);
    };

    var focusedQuestion = "";

});