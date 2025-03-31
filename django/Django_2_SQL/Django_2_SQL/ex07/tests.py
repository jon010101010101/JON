from django.test import TestCase
from django.urls import reverse
from .models import Movie
from django.utils import timezone

class MovieModelTests(TestCase):
    def test_create_movie(self):
        movie = Movie.objects.create(
            episode_nb=1,
            title="Test Movie",
            director="Test Director",
            producer="Test Producer",
            release_date="2000-01-01"
        )
        self.assertEqual(movie.title, "Test Movie")
        self.assertIsNotNone(movie.created)
        self.assertIsNotNone(movie.updated)
        self.assertTrue(movie.created <= timezone.now())
        self.assertTrue(movie.updated <= timezone.now())
        self.assertEqual(str(movie), "Test Movie")

class PopulateViewTests(TestCase):
    def test_populate_view(self):
        response = self.client.get(reverse('populate'))
        self.assertEqual(response.status_code, 200)
        self.assertIn("OK", response.content.decode())
        self.assertEqual(Movie.objects.count(), 7)

class DisplayViewTests(TestCase):
    def test_display_view_no_data(self):
        response = self.client.get(reverse('display'))
        self.assertEqual(response.status_code, 200)
        self.assertIn("No data available", response.content.decode())

    def test_display_view_with_data(self):
        Movie.objects.create(
            episode_nb=1,
            title="Test Movie",
            director="Test Director",
            producer="Test Producer",
            release_date="2000-01-01"
        )
        response = self.client.get(reverse('display'))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn("No data available", response.content.decode())
        self.assertIn("Test Movie", response.content.decode())

class UpdateViewTests(TestCase):
    def test_update_view_no_data(self):
        response = self.client.get(reverse('update'))
        self.assertEqual(response.status_code, 200)
        self.assertIn("No data available", response.content.decode())

    def test_update_view_with_data(self):
        movie = Movie.objects.create(
            episode_nb=1,
            title="Test Movie",
            director="Test Director",
            producer="Test Producer",
            release_date="2000-01-01"
        )
        response = self.client.get(reverse('update'))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn("No data available", response.content.decode())
        self.assertIn(movie.title, response.content.decode())

    def test_update_movie(self):
        movie = Movie.objects.create(
            episode_nb=1,
            title="Test Movie",
            director="Test Director",
            producer="Test Producer",
            release_date="2000-01-01"
        )
        response = self.client.post(reverse('update'), {
            'movie_id': movie.episode_nb,
            'opening_crawl': 'New opening crawl text'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("OK: Movie 'Test Movie' updated successfully.", response.content.decode())
        movie.refresh_from_db()
        self.assertEqual(movie.opening_crawl, 'New opening crawl text')