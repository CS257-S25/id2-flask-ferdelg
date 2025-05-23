"""
data.py

The purpose of this module is to import and process datasets from various streaming services.
It creates a 3D list of media entries and a dictionary indexed by title for easy access.
"""
import csv
from ProductionCode import formatting

# Constants for the indices of dataset columns to make indexing easier.
SHOW_ID = 0
MEDIA_TYPE = 1
TITLE = 2
DIRECTOR = 3
CAST = 4
COUNTRY = 5
DATE_ADDED = 6
RELEASE_YEAR = 7
RATING = 8
DURATION = 9
LISTED_IN = 10
DESCRIPTION = 11
STREAMING_SERVICE = 12

class Data:
    """A class to represent the dataset of movies and shows from various streaming services"""

    def __init__(self):
        """
        Initializes the Data class by importing datasets from various streaming services
        and creating a list and dictionary of media entries.
        """
        self.media_list = import_all_datasets_to_list()
        self.media_dict = create_media_dict_by_title(self.media_list)
        self.category_set = create_category_set(self.media_list)

    def get_media_list(self):
        """
        Returns the list containing data for all shows/movies from all streaming services.
        [<service>, <row>, <column>]
        """
        return self.media_list

    def get_media_dict(self):
        """
        Returns the dictionary containing data for all shows/movies from all streaming services.
        {<title>: <Media object>}
        """
        return self.media_dict

    def get_category_set(self):
        """
        Returns a set containing all of the categories named within the data.
        """
        return self.category_set

    def print_media_list(self):
        """
        Prints the entire media list, including the data from all 4 streaming services.
        """
        for service in self.media_list:
            print(f"STREAMING SERVICE: {service}\n")
            for entry in service:
                print(f"{entry}\n")


class Media:
    """
    A class to represent a single movie or show entry from the dataset
    and all of its associated information.
    """

    def __init__(self, entry):
        fill_empty_fields(entry)
        self.attributes = []
        self.attributes.append(entry[SHOW_ID])
        self.attributes.append(entry[MEDIA_TYPE])
        self.attributes.append(entry[TITLE])
        self.attributes.append(formatting.make_set(entry[DIRECTOR]))
        self.attributes.append(formatting.make_set(entry[CAST]))
        self.attributes.append(formatting.make_set(entry[COUNTRY]))
        self.attributes.append(entry[DATE_ADDED])
        self.attributes.append(entry[RELEASE_YEAR])
        self.attributes.append(entry[RATING])
        self.attributes.append(entry[DURATION])
        self.attributes.append(formatting.make_set(entry[LISTED_IN]))
        self.attributes.append(entry[DESCRIPTION])
        self.attributes.append(formatting.make_set(entry[STREAMING_SERVICE]))

    def get_show_id(self):
        """Returns the media's show id."""
        return self.attributes[SHOW_ID]
    def get_media_type(self):
        """Returns the media's type."""
        return self.attributes[MEDIA_TYPE]
    def get_title(self):
        """Returns the media's title."""
        return self.attributes[TITLE]
    def get_director(self):
        """Returns the media's director."""
        return self.attributes[DIRECTOR]
    def get_cast(self):
        """Returns the media's cast."""
        return self.attributes[CAST]
    def get_country(self):
        """Returns the media's country."""
        return self.attributes[COUNTRY]
    def get_date_added(self):
        """Returns the media's date added."""
        return self.attributes[DATE_ADDED]
    def get_release_year(self):
        """Returns the media's release year."""
        return self.attributes[RELEASE_YEAR]
    def get_rating(self):
        """Returns the media's rating."""
        return self.attributes[RATING]
    def get_duration(self):
        """Returns the media's duration."""
        return self.attributes[DURATION]
    def get_category(self):
        """Returns the media's category."""
        return self.attributes[LISTED_IN]
    def get_description(self):
        """Returns the media's description."""
        return self.attributes[DESCRIPTION]
    def get_streaming_service(self):
        """Returns the media's streaming service."""
        return self.attributes[STREAMING_SERVICE]
    def str(self):
        """
        Gets representation of individual media objects as a string.
        """
        return (f"Title: {self.get_title()}\n"
            f"Show ID: {self.get_show_id()}\n"
            f"Media Type: {self.get_media_type()}\n"
            f"Director: {self.get_director()}\n"
            f"Cast: {self.get_cast()}\n"
            f"Country: {self.get_country()}\n"
            f"Date Added: {self.get_date_added()}\n"
            f"Release Year: {self.get_release_year()}\n"
            f"Rating: {self.get_rating()}\n"
            f"Duration: {self.get_duration()}\n"
            f"Listed In: {self.get_category()}\n"
            f"Description: {self.get_description()}\n"
            f"Streaming Services: {self.get_streaming_service()}")


def import_all_datasets_to_list(
    netflix_dataset="Data/dummy_netflix.csv",
    amazon_dataset="Data/dummy_amazon.csv",
    disney_dataset="Data/dummy_disney.csv",
    hulu_dataset="Data/dummy_hulu.csv",
):
    """
    Imports datasets from various streaming services and returns a list containing the data of 
    all 4.
    """
    netflix_data = []
    amazon_prime_data = []
    disney_plus_data = []
    hulu_data = []

    import_dataset_to_list(netflix_dataset, netflix_data, "Netflix")
    import_dataset_to_list(amazon_dataset, amazon_prime_data, "Amazon Prime")
    import_dataset_to_list(disney_dataset, disney_plus_data, "Disney+")
    import_dataset_to_list(hulu_dataset, hulu_data, "Hulu")

    media_list = [netflix_data, amazon_prime_data, disney_plus_data, hulu_data]
    return media_list


def import_dataset_to_list(dataset, data, streaming_service_name):
    """
    Imports the each cell from a CSV file into a list of rows
    and appends the streaming service name to each row.
    """
    with open(dataset, encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            row.append(streaming_service_name)
            data.append(row)


def create_media_dict_by_title(data):
    """
    Creates a dictionary of media entries indexed by their titles.
    Each entry is a Media object containing all the information about the movie or show.
    """
    media_dict = {}
    for streaming_service in data:
        for entry in streaming_service:
            # Create a Media object for each row
            media = Media(entry)
            _add_media_to_dict_by_title(media, media_dict)
    media_dict = formatting.sort_dict_by_key(media_dict)
    return media_dict


def _add_media_to_dict_by_title(media, media_dict):
    """
    Adds a Media object to the dictionary indexed by its title.
    If the title already exists, it adds another streaming service to the existing entry.
    """
    title = media.get_title()

    if title not in media_dict:
        media_dict[title] = media
    else:
        for service in media_dict[title].get_streaming_service():
            media_dict[title].get_streaming_service().add(service)

def create_category_set(data):
    """
    Creates a set containing all the unique catergories named within all 4 datasets.
    """
    categories = set()
    for streaming_service in data:
        for entry in streaming_service:
            listed_categories = formatting.make_set(entry[LISTED_IN])
            for category in listed_categories:
                categories.add(category)
    return categories

def fill_empty_fields(entry):
    """
    Fills empty fields in the entry with "Unspecified" to avoid issues with missing data.
    """
    for field in entry:
        if field == "":
            field = "Unspecified"

def main():
    """
    Main function to test the Data class and its methods.
    """

if __name__ == "__main__":
    main()
