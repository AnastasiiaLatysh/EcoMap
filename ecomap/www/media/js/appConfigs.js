app.config(['$stateProvider', '$urlRouterProvider', '$authProvider', function($stateProvider, $urlRouterProvider, $authProvider) {

  $stateProvider
    .state('user_profile', {
      url: '/user_profile',
      templateUrl: '/templates/userProfile.html',
      controller: 'UserProfileCtrl'
    })
    .state('map', {
      url: '/map',
      templateUrl: '/templates/map.html',
      controller: 'MapCtrl'
    })
    .state('admin', {
      url: '/admin',
      templateUrl: '/templates/admin.html',
      controller: 'AdminCtrl'
    })
    .state('faq', {
      url: '/faq/:faqAlias',
      templateUrl: '/templates/detailedFaq.html',
      controller: 'DetailedFaqCtrl'
    })
    .state('addFaq', {
      url: '/addFaq',
      templateUrl: '/templates/addFaq.html',
      controller: 'AddFaqCtrl'
    })
    .state('editFaq', {
      url: '/editFaq/:id',
      templateUrl: '/templates/editFaq.html',
      controller: 'EditFaqCtrl'
    })
    .state('login', {
      url: '/login',
      onEnter: ['$stateParams', '$state', '$uibModal', function($stateParams, $state, $uibModal) {
        $uibModal.open({
            templateUrl: '/templates/login.html',
            controller: 'LoginCtrl',
        }).result.finally(function() {
            $state.go('map');
        });
      }]
    })
    .state('register', {
      url: '/register',
      onEnter: ['$stateParams', '$state', '$uibModal', function($stateParams, $state, $uibModal) {
        $uibModal.open({
            templateUrl: '/templates/register.html',
            controller: 'RegisterCtrl',
        }).result.finally(function() {
            $state.go('map');
        });
      }]
    });
    
    $urlRouterProvider.otherwise('/map');
    $authProvider.loginUrl = '/api/login';
    $authProvider.signupUrl = '/api/register';    

}]);
