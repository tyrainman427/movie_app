$(document).ready(function (){
  $('#searchForm').on('submit',(e) => {
    let searchText = $('#searchText').val();
    var res = searchText.replace(" ", "%20");
    console.log(res)
    getMovies(res)
    e.preventDefault();
  });
});


function getMovies(searchText){
  axios.get('https://www.omdbapi.com/?s=' + searchText  + '&apikey=5aaeba44')
    .then((response) => {

      let movies = response.data.Search
      let output = '';
      $.each(movies,(index, movie) => {
        output += `
                  <div class="card mr-4 mb-3 text-center">
                    <img class="img-fluid" src="${movie.Poster}" alt="${movie.Title} image">
                    <div class="card-body">
                    <h5 class="card-title">${movie.Title}</h5>
                    <a onclick="movieSelected('${movie.imdbID}')" class="btn btn-primary" style="color:white;">Movie Details</a>
                </div>
                </div>
        `;

      })
      $('#movie').html(output)
    })
    .catch((err)=> {
      console.log(err);
    });
}

function movieSelected(id) {
    sessionStorage.setItem('movieId',id);
    window.location = 'details/';
    return false;
}

function getMovie() {
  let movieId = sessionStorage.getItem('movieId')

  axios.get('https://www.omdbapi.com/?i=' + movieId  + '&apikey=5aaeba44')
    .then((response) => {

      let movie = response.data

      let output = `
      <div class="row">
        <div class="col-md-4">
          <img src="${movie.Poster}" class="thumbnail">
          </div>
          <div class="col-md-8">
            <h2>${movie.Title}</h2>
            <ul class="list-group">
              <li class="list-group-item"><strong>Genre:</strong> ${movie.Genre}</li>
              <li class="list-group-item"><strong>Released:</strong> ${movie.Released}</li>
              <li class="list-group-item"><strong>Rated:</strong> ${movie.Rated}</li>
              <li class="list-group-item"><strong>Imdb Rating:</strong> ${movie.imdbRating}</li>
              <li class="list-group-item"><strong>Director:</strong> ${movie.Director}</li>
              <li class="list-group-item"><strong>Writer:</strong> ${movie.Writer}</li>
              <li class="list-group-item"><strong>Actors:</strong> ${movie.Actors}</li>
            </ul>
          </div>
        </div>
        <div class="row">
        <div class="well">
          <h3>Plot</h3>
          ${movie.Plot}
          <hr>
          <a href="/" class="btn btn-secondary">Go Back To Search</a>
        </div>
        </div>
      `;
      $('#movie').html(output)
    })
    .catch((err)=> {
      console.log(err);
    });
  }


// apikey = 5a9a499aab6b68363c15ff758505f74f
