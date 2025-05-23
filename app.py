"""
ID2 flask app.
"""

from flask import Flask
from ProductionCode.filtering import Filter
from ProductionCode.data import Data
from ProductionCode.formatting import make_list_web_displayable

app = Flask(__name__)
dataset = Data()
filtering = Filter(dataset)

@app.route('/')
def homepage():
    """
    Determines the text on the homepage of the website. 
    Displays detailed instructions regarding the usage of the application.
    """
    return (
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


@app.route('/actor/<name>', strict_slashes=False)
def search_by_actor(name):
    """
    Returns movie titles that feature the specified actor.

    Parameter:
        name (str): The name of the actor searched for.

    Returns:
        str: A string listing matching movie titles.
    """
    results = filtering.filter_by_actor(name)
    return make_list_web_displayable(results.get_titles_list())
if __name__ == "__main__":
    app.run()
