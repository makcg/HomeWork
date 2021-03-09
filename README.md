# HomeWork 12

select name, flname from films inner join films_actors on (films.id = films_actors.film_id) inner join actors on (films_actors.actors_id = actors.id);
