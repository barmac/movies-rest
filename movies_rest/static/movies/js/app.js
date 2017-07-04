/**
 * Created by maciej on 04.07.17.
 */
$(document).ready(function () {

    function getMovies() {
        $.ajax({
          url: 'http://127.0.0.1:8000/movies',
          type: 'GET'
        })
            .done(function(response, state) {
              console.log(response);
            })
            .fail(function(response, state) {
                console.log('fail')
            });
    }

    function postMovie(movie) {
        $.ajax({
            url: 'http://127.0.0.1:8000/movies',
            type: 'POST',
            data: movie
        })
            .done(function (response, state) {
                console.log(response);
            })
            .fail(function (response, state) {
                console.log('fail')
            });
    }

    function getMovie(id) {
        $.ajax({
            url: 'http://127.0.0.1:8000/movies/' + id,
            type: 'GET'
        })
            .done(function(response, state) {
                console.log(response);
            })
            .fail(function(response, state) {
                console.log('fail')
            });
    }

    function deleteMovie(id) {
        $.ajax({
            url: 'http://127.0.0.1:8000/movies' + id,
            type: 'DELETE'
        })
            .done(function (response, state) {
                console.log(response);
            })
            .fail(function (response, state) {
                console.log('fail')
            });
    }

    function putMovie(id) {
        $.ajax({
            url: 'http://127.0.0.1:8000/movies' + id,
            type: 'PUT'
        })
            .done(function (response, state) {
                console.log(response);
            })
            .fail(function (response, state) {
                console.log('fail')
            });
    }

    function getPeople() {
        $.ajax({
          url: 'http://127.0.0.1:8000/people',
          type: 'GET'
        })
            .done(function(response, state) {
              console.log(response);
            })
            .fail(function(response, state) {
                console.log('fail')
            });
    }

    function postPerson(movie) {
        $.ajax({
            url: 'http://127.0.0.1:8000/people',
            type: 'POST',
            data: movie
        })
            .done(function (response, state) {
                console.log(response);
            })
            .fail(function (response, state) {
                console.log('fail')
            });
    }

    function getPerson(id) {
        $.ajax({
            url: 'http://127.0.0.1:8000/people/' + id,
            type: 'GET'
        })
            .done(function(response, state) {
                console.log(response);
            })
            .fail(function(response, state) {
                console.log('fail')
            });
    }

    function deletePerson(id) {
        $.ajax({
            url: 'http://127.0.0.1:8000/people' + id,
            type: 'DELETE'
        })
            .done(function (response, state) {
                console.log(response);
            })
            .fail(function (response, state) {
                console.log('fail')
            });
    }

    function putPerson(id) {
        $.ajax({
            url: 'http://127.0.0.1:8000/people' + id,
            type: 'PUT'
        })
            .done(function (response, state) {
                console.log(response);
            })
            .fail(function (response, state) {
                console.log('fail')
            });
    }

//    tests
    getMovies();
    getMovie(1);
    getPeople();
    getPerson(1);
});
