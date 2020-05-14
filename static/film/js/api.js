var settings = {
	"async": true,
	"crossDomain": true,
	"url": "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/search/inception",
	"method": "GET",
	"headers": {
		"x-rapidapi-host": "imdb-internet-movie-database-unofficial.p.rapidapi.com",
		"x-rapidapi-key": "bff6c04355msh46e32c3afb8d323p1eaeedjsnbf048a37783e"
	}
}

$.ajax(settings).done(function (response) {
	console.log(response);
});
