import pytest

from fastapi.testclient import TestClient

from app.main import app

class TestPages():
    """
    Tests to check the action/responses of different pages. Can be split to different
    classes when neccesary.
    """
    success_response_template = {
        "Result": 1,
        "Message": None,
        "DataObject": None,
    }

    def test_get_main(self, client: TestClient):
        """Check if GET '/' can return expected value."""
        response = client.get('/')
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}

    def test_get_team_info(self, client: TestClient):
        """Check if team's page '/teams/<id> returns correct response in GET method."""
        response = client.get('/teams/2')
        assert response.status_code == 200
        
        # Check response json
        team_info = {
            "ID": 2,
            "TeamName": "test team0",
            "DepartureDate": "2022-11-06",
            "ReturnDate": "2022-11-08",
            "GuideID": 5,
            "LeaderID": 4
        }
        expected_response = self.success_response_template.copy()
        expected_response["DataObject"] = team_info
        assert response.json() == expected_response

    def test_create_and_retrieve_team_info(self, client: TestClient):
        """
        Check if user can create a new team info via teams/new and
        use the retrieved ID to get the new team info.
        """
        new_team_info = {
            "TeamName": "I love hiking!",
            "DepartureDate": "2022-11-08",
            "ReturnDate": "2022-11-10",
            "GuideID": 2,
            "LeaderID": 3
        }
        response = client.post('/teams/new', json=new_team_info)

        # check POST result
        assert response.status_code == 200

        # GET the team info by id retreived from the POST request and compare
        # the result
        new_team_id = response.json()["DataObject"]['NewTeamID']
        response = client.get(f"/teams/{new_team_id}")
        # add id to the new team info for comparison
        new_team_info["ID"] = new_team_id
        expected_response = self.success_response_template.copy()
        expected_response["DataObject"] = new_team_info
        assert response.json() == expected_response
