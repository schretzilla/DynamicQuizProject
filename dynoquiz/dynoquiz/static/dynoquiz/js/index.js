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
		$http.post('/dynoquiz/api/quiz/', quiz);
		$scope.loadItems();

	};

	//Check
	$scope.deleteQuiz = function(id) {
		alert("attempt delete: " + id);
		$http.delete('/dynoquiz/api/quiz/' + id).then(function(){
			$scope.loadItems();
		});
		//$scope.loadItems();
	};

	$scope.toggleCreateQuiz = function() {
		$scope.createQuizFields = !$scope.createQuizFields;
	};

	$scope.loadItems();
	$scope.createQuizFields = false;


}); //End Index controller 