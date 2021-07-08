
from functools import lru_cache

import requests
from flask import Flask, request, jsonify
from flask_restful import Api, Resource

route_1 = "/api/ping"
route_2 = "/api/posts"


# Application factory
def create_app(test_config=None):
    app = Flask(__name__)
    api = Api(app)

    class Ping(Resource):
        def get(self):
            return {"success": True}, 200

    class Blog(Resource):

        @lru_cache()
        def get(self):


            # Error messages
            error_tag_responses = {"error": "Tags parameter is required"}
            error_sort_by_responses = {"error": "sortBy parameter is invalid"}
            error_direction_responses = {"error": "direction parameter is invalid"}
            error_unclear_responses = {
                "error": "Possible Network/Internet connection error."
            }
            # Parse URL arguments/parameters
            tags_string = request.args.get("tags", None, str)
            if tags_string is None:
                return error_tag_responses, 400

            sort_by = request.args.get("sortBy", "id")
            if sort_by not in ["id", "reads", "likes", "popularity"]:
                return error_sort_by_responses, 400

            direction = request.args.get("direction", "asc")
            if direction not in ["asc", "desc"]:
                return error_direction_responses, 400

            tags = tags_string.strip().lower().split(",")

            # Send HTTP GET request to gather data from provider
            try:
                data = []
                for tag in tags:
                    # print(tag)
                    resp = requests.get(
                        f"https://api.hatchways.io/assessment/solution/posts?tags={tag}"
                    ).json()
                    data += resp["posts"]

                # Sort in-place based on desired (parameters) criteria
                is_reverse = True if direction == "desc" else False

                # data.sort(key=lambda x: x[sort_by], reverse=is_reverse)
                data = sorted(data, key=lambda x: x[sort_by], reverse=is_reverse)

                return {"posts": data}, 200

            except:
                return error_unclear_responses, 400

    # Resources
    api.add_resource(Ping, route_1)
    api.add_resource(Blog, route_2)

    # Error handlers for expected errors including 404 and 422.
    @app.errorhandler(400)
    def bad_request(error):
        error_message = (
            "The server could not understand the request due to invalid syntax."
        )
        return jsonify({"success": False, "error": 400, "message": error_message}), 400

    @app.errorhandler(404)
    def requested_method_not_found(error):
        error_message = (
            "The server can not find requested resource. "
            "The endpoint may be valid but the resource itself does not exist."
        )
        return jsonify({"success": False, "error": 404, "message": error_message}), 404

    return app
