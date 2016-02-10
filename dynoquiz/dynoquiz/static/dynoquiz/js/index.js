var index = angular.module('index',[]);

index.config(function($interpolateProvider){
	//allow django templates and angular to co-exist
	$interpolateProvider.startSymbol('{[{');
	$interpolateProvider.endSymbol('}]}');
});

index.controller('QuizCtrl', function QuizCtrl($scope, $log, $http){
	
	$scope.loadItems = function() {
		$http.get('/dynoquiz/api/quiz/').then(function(response){
			$scope.quizes = response.data.reverse();
		});
	}; // End loadItems 

	$scope.addQuiz = function(){
		$scope.date = new Date();
		quiz = {
			'quiz_name':$scope.quizName,
			'quiz_details':$scope.quizDetails,
			'date_created':$scope.date
		};
		$scope.quizName=null;
		$scope.quizDetails=null;
		//TODO: Check why refresh is needed to see results here
		$http.post('/dynoquiz/api/quiz/', quiz).then(function(){
			$scope.loadItems();
		});
	};

	$scope.updateQuiz = function(){

	};

	$scope.deleteQuiz = function(id) {
		$http.delete('/dynoquiz/api/quiz/' + id).then(function(){
			$scope.loadItems();
		});
	};

	$scope.toggleCreateQuiz = function() {
		$scope.createQuizFields = !$scope.createQuizFields;
	};

	$scope.formsetEditQuiz = function(quiz) {
	    $scope.updateQuizBtn = true;
	    $scope.editBtnClass = "active";
	    $scope.createBtnClass = "";
	    $scope.createQuizBtn = false;
	    $scope.quizName = quiz.quiz_name;
	    $scope.quizDetails = quiz.quiz_details;
	};

	$scope.formsetCreateQuiz = function() {
	    $scope.updateQuizBtn = false;
	    $scope.editBtnClass="disabled";
	    $scope.createBtnClass="active";
	    $scope.createQuizBtn = true;
	    $scope.quizName = "";
	    $scope.quizDetails = "";

	}

	$scope.loadItems();
	$scope.formsetCreateQuiz();


}); //End Index controller 