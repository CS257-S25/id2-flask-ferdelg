"""
test_app.py

This module contains unit tests for the StreamSearch web app.
It tests the functionality of the homepage and actor route.
"""

import unittest
import app

class TestHomepage(unittest.TestCase):
    """Test the homepage route to ensure it has the correct content."""

    def test_homepage(self):
        """Check if the homepage function returns the correct content."""
        expected_homepage = (
        """
        <h1>Welcome to the StreamSearch Homepage! <3</h1></br></br>
        StreamSearch can help you find movies and TV shows from a specific actor!</br></br>
        <b>To Use enter the following:</b></br>
        * <b>[URL]/actor/name</b>: Enter the name of an actor to 
        find movies or shows they appear in. </br>
        <b>Try this example:</b></br>
        [URL]/actor/Emma Stone</br>
        """
        )
        self.assertEqual(app.homepage(), expected_homepage)


class TestFilterFunctions(unittest.TestCase):
    """Test class for the Filter class and its methods."""
    def test_actor_filter(self):
        """Check if filtering by actor includes the correct titles."""
        self.assertIn(
            "The Grand Seduction",
            app.search_by_actor("Brendan Gleeson")
            )

    def test_actor_filter_lowercase(self):
        """Check if filtering with all fields in lowercase includes only correct titles."""
        self.assertEqual(
            app.search_by_actor("brendan gleeson"),
            "The Grand Seduction"
        )

    def test_actor_filter_mixedcase(self):
        """Check if filtering with all fields in mixedcase includes only correct titles."""
        self.assertEqual(
            app.search_by_actor("bReNdan GleEsOn"),
            "The Grand Seduction"
        )

    def test_actor_filter_uppercase(self):
        """Check if filtering with all fields in uppercase includes only correct titles."""
        self.assertEqual(
            app.search_by_actor("BRENDAN GLEESON"),
            "The Grand Seduction"
        )

    def test_nonexistents_actor(self):
        """Check if filtering by a nonexistent actor results in an empty string."""
        self.assertEqual(
            app.search_by_actor("Maria-del-granado"), 
            ""
        )

if __name__ == "__main__":
    unittest.main()
