# Demand Tracking

This project is a management system and blog for displaying and managing information of various regions such as counties, cities, districts, and villages. For each region, information such as opportunities, threats, weaknesses, and capacities are recorded and managed.

## Related Project

This backend project is synchronized and connected to a website developed with Vue.js. The website allows users to interact with the backend and receive the necessary information and services. For more information about the Vue.js website, please visit [Demand Tracking](https://github.com/Fatemi-abasaleh/).

## Project Features

- **Region Categorization**: Includes counties, cities, districts, villages, etc.
- **Key Features**: Each section has features like opportunities, threats, weaknesses, and capacities, each with its sub-features.
- **Connecting Sub-features to Regions**: Each sub-feature is linked to a section of the region (e.g., village or city) and includes information such as title, description, photos, etc.
- **Response by Organizations**: It can be determined which organization or authority is responsible for responding to each feature, and their responses are stored as well.
- **Neighborhood Information**: Includes the name, photos, and notable people of that neighborhood.
- **Information Transparency**: All information, including features and responses, is publicly viewable in the blog section to ensure transparency in presenting information.

## Key Models

### 1. APIKEY
This model is used to manage API keys, specifying whether the key is for the admin panel or the blog.

### 2. Character
This model defines different roles with access levels (chief admin, representative, and manager). Each role has an access level that determines their access to different system sections.

### 3. Manager
The Manager model stores personal and professional information of managers responsible for each region. This includes name, contact number, national ID, password, and character (role) of the manager. Managers can be edited or removed.

### 4. LocationBelongToManager
This model links managers to the regions they manage. The connection between a manager and the regions they oversee is managed through this model.

### 5. BigCity, City, CityPart, BigVillage, Village
These models store information about various places, from large cities to villages. Each model includes information such as code, name, population, household count, images, and descriptions of the area. Connections between different areas are also managed through these models.

### 6. Proper
This model defines additional or "special" features related to places and people. These features can include properties, infrastructure, etc., which can be linked to different areas.

### 7. PeopleBelongLocation
This model stores information about people related to a specific area, including name, family, special feature (Proper), and an attached file if available. It can also identify notable people associated with that region.

### 8. Property and SubProperty
These models define general features and sub-features. Features like opportunities, threats, weaknesses, and capacities are managed through these models and are linked to specific places (like villages, cities, or districts).

### 9. PropertyBelongPlace
This model links specific features (like infrastructure, economic opportunities, etc.) to particular places. This model includes information such as the feature's title, description, images, and whether the feature is private or public.

### 10. AnswerToProperty
This model stores responses given by organizations or managers to each feature. Responses include content, attached files, and the last edited time.

### 11. RedundantInformation
This model stores additional and unnecessary information related to various places, which may not seem essential initially but may become useful in the future.

### 12. ReInformationValue
This model stores values related to the additional information from the "RedundantInformation" model. Each additional value is tied to a specific place and stored as textual data.

### 13. Section
This model defines different sections of the system. Each role can have access to specific sections through this model.

### 14. AccessCharacter
This model determines which sections of the system each role has access to. For example, a chief admin may have access to all sections, while a manager might only have access to a specific section.

### 15. ExportPropertyList
This model manages the export list of features related to places and can export them in various formats.

### 16. Organization
This model stores information about organizations or agencies that are connected to the project and may be responsible for responding to the features.

### 17. SolutionBelongToProperty
This model stores solutions provided by organizations for various features. Each solution is tied to a specific feature and organization.

### 18. Slider
This model stores images related to the slider on the blog or admin panel page, including information like the image and the time it was uploaded.

## Prerequisites

To run this project, you need to have the following software and tools installed:

- [Python](https://www.python.org/downloads/) version 3.8 or higher
- [Django](https://www.djangoproject.com/) version 3.2 or higher

## Project Dependencies

The following packages are used in this project:

- `Django==5.0.1`
- `django-cors-headers==4.3.0`
- `django-jalali==6.0.1`
- `djangorestframework==3.14.0`
- `jdatetime==5.0.0`

  ## Installation and Setup

Follow these steps to set up the project:

1. Clone the repository:

    ```bash
    git clone https://github.com/Bestsenator/DemandTracking.git
    ```

2. Navigate to the project directory:

    ```bash
    cd DemandTracking
    ```

3. Create a Python virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS or Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install the project dependencies:

    ```bash
    pip install -r req.txt
    ```

6. Configure the `.env` file based on the `.env.example` template.

7. Apply the database migrations:

    ```bash
    python manage.py migrate
    ```

8. Run the server:

    ```bash
    python manage.py runserver
    ```

9. The project is now available at `http://localhost:8000`.

## API Endpoints

The following APIs are provided for interacting with data and managing various sections of the project:

### Authentication & Session Management
- `POST /loginCheck/`: Check login status.
- `GET /checkSession/`: Check user session status.

### Location Management
- `GET /getLocationListByFilter/`: Get a list of locations with filters.
- `GET /getRedundantLocation/`: Get redundant locations.
- `GET /getAllRedundant/`: Get all redundant locations.
- `POST /addRedundantForLocation/`: Add a redundant location for a place.
- `POST /editRedundantForLocation/`: Edit a redundant location for a place.
- `POST /deleteRedundantForLocation/`: Delete a redundant location for a place.
- `POST /addPlace/`: Add a new place.
- `GET /getCityList/`: Get a list of cities.
- `GET /getBigCityList/`: Get a list of major cities.
- `GET /getCityPartList/`: Get a list of city parts.
- `GET /getBigVillageList/`: Get a list of major villages.
- `GET /getVillageList/`: Get a list of villages.
- `POST /deletePlace/`: Delete a place.
- `POST /editPlace/`: Edit a place.
- `GET /getInfoPlace/`: Get information about a place.

### Property Management
- `GET /getPropertyListByFilter/`: Get a list of properties with filters.
- `GET /getInfoPropertyBToPlace/`: Get property information related to a place.
- `POST /deletePropertyBelongToPlace/`: Delete a property related to a place.
- `GET /getPropertyNameList/`: Get a list of property names.
- `GET /getAllSubPropertyNameList/`: Get a list of all sub-property names.
- `GET /getSubPropertyNameList/`: Get a list of sub-property names.
- `POST /addPropertyToPlace/`: Add a property to a place.
- `POST /editPropertyToPlace/`: Edit a property related to a place.
- `POST /addSubProperty/`: Add a sub-property.
- `POST /editSubProperty/`: Edit a sub-property.
- `POST /deleteSubProperty/`: Delete a sub-property.

### People Management
- `GET /getProperList/`: Get a list of people.
- `GET /getPeopleBelongToPlaceList/`: Get a list of people related to a place.
- `GET /getInfoPeopleBelongToPlace/`: Get information about a person related to a place.
- `POST /addPeopleBelongToPlace/`: Add a person to a place.
- `POST /editPeopleBelongToPlace/`: Edit a person related to a place.
- `POST /deletePeopleBelongToPlace/`: Delete a person from a place.

### Answer & Solution Management
- `GET /getAnswerPropertyBToPlaceList/`: Get a list of answers for properties related to a place.
- `POST /addAnswerToProperty/`: Add an answer to a property.
- `POST /editAnswerProperty/`: Edit an answer for a property.
- `POST /deleteAnswerProperty/`: Delete an answer for a property.
- `GET /getFullInfoPropertyBToPlace/`: Get complete information about a property related to a place.
- `GET /getSolutionToProperty/`: Get solutions related to a property.
- `POST /addSolutionToProperty/`: Add a solution to a property.
- `POST /editSolutionToProperty/`: Edit a solution related to a property.
- `POST /deleteSolutionToProperty/`: Delete a solution related to a property.

### Manager Management
- `GET /getAccessListManager/`: Get a list of manager access permissions.
- `GET /getCharacterList/`: Get a list of roles.
- `POST /addManager/`: Add a manager.
- `POST /editManager/`: Edit a manager.
- `POST /deleteManager/`: Delete a manager.
- `POST /addLocationToManager/`: Add a location to a manager.
- `POST /deleteLocationToManager/`: Remove a location from a manager.
- `GET /getLocationListByPhrase/`: Get a list of locations based on a phrase.
- `GET /getInfoPropertyLocation/`: Get information about property related to a location.
- `GET /getManagerList/`: Get a list of managers.
- `GET /getManagerInfo/`: Get information about a manager.

### Export & Slider Management
- `GET /exportToDatabase/`: Export data to the database.
- `GET /getSlider/`: Get a list of sliders.
- `POST /addSlider/`: Add a slider.
- `POST /deleteSlider/`: Delete a slider.

### Access Management
- `GET /getAccessLocationList/`: Get a list of location access permissions.
- `GET /getLocationListBlog/`: Get a list of locations for the blog.

Note: The APIs are written using Postman, and the collections are available at [postmanCollection](https://github.com/Bestsenator/DemandTracking/blob/master/postmanCollection/API.postman_collection.json).

## Project Structure
```
DemandTracking/
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── api/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── index/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── funcs/
│   ├── check.py
│   └── verify.py
├── media/
│   ├── locationImage
│   ├── peopleBelongToPlace
│   ├── propertyBelongToPlace
│   └── slider
├── static/
├── manage.py
├── db.sqlite3
├── README.md
├── README_fa.md
├── README_en.md
└── req.txt
```
## Contributing

If you would like to contribute to this project, you can:

1. Fork this repository.
2. Create a new branch for your feature or bug fix (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push your branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## Special Thanks

[Seyed Abasaleh Fatemi](https://github.com/Fatemi-abasaleh)

Special thanks to the Vue.js front-end developer who skillfully developed this website and integrated it with the back-end system. Without his efforts, creating this integrated system would not have been possible.
