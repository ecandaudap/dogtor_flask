from flask import Flask, request


def create_app():
    app = Flask(__name__)

    users = [
        {"id": 1, "username": "user0", "email": "user0@kodemia.mx"},
        {"id": 2, "username": "user1", "email": "user1@kodemia.mx"},
        {"id": 3, "username": "user2", "email": "user2@kodemia.mx"},
    ]

    @app.post("/users/auth")
    def auth():
        data = request.data
        return data

    @app.route("/users/<int:user_id>", methods=["GET", "PUT", "DELETE"])
    @app.route("/users/", methods=["GET", "POST"])
    def users_endpoint(user_id=None):
        if user_id is not None:
            found_user = None
            for user in users:
                if user["id"] == user_id:
                    found_user = user

            if request.method == "PUT":
                return {"detail": f"user {found_user['username']} modified"}
            if request.method == "DELETE":
                return {"detail": f"user {found_user['username']} deleted"}

            return found_user

        if request.method == "POST":
            data = request.data
            return {"detail": f"user {data['username']} created"}
        return users

    @app.route("/home")
    @app.route("/")
    def hello():
        return "Hello Koders!"

# owners

    owners = [
            {"id": 1, "ownername": "owner0", "email": "owner0@kodemia.mx"},
            {"id": 2, "ownername": "owner1", "email": "owner1@kodemia.mx"},
            {"id": 3, "ownername": "owner2", "email": "owner2@kodemia.mx"},
        ]

    @app.post("/owners/auth")
    def auth_owner():
        data = request.data
        return data

    @app.route("/owners/<int:owner_id>", methods=["GET", "PUT", "DELETE"])
    @app.route("/owners/", methods=["GET", "POST"])
    def owners_endpoint(owner_id=None):
        if owner_id is not None:
            found_owner = None
            for owner in owners:
                if owner["id"] == owner_id:
                    found_owner = owner

            if request.method == "PUT":
                return {"detail": f"owner {found_owner['ownername']} modified"}
            if request.method == "DELETE":
                return {"detail": f"owner {found_owner['ownername']} deleted"}

            return found_owner

        if request.method == "POST":
            data = request.data
            return {"detail": f"owner {data['ownername']} created"}
        return owners

# pets

    pets = [
            {"id": 1, "petname": "pet0", "owner": "owner0"},
            {"id": 2, "petname": "pet1", "owner": "owner1"},
            {"id": 3, "petname": "pet2", "owner": "owner2"},
        ]

    @app.post("/pets/auth")
    def auth_pet():
        data = request.data
        return data

    @app.route("/pets/<int:pet_id>", methods=["GET", "PUT", "DELETE"])
    @app.route("/pets/", methods=["GET", "POST"])
    def pets_endpoint(pet_id=None):
        if pet_id is not None:
            found_pet = None
            for pet in pets:
                if pet["id"] == pet_id:
                    found_pet = pet

            if request.method == "PUT":
                return {"detail": f"pet {found_pet['petname']} modified"}
            if request.method == "DELETE":
                return {"detail": f"pet {found_pet['petname']} deleted"}

            return found_pet

        if request.method == "POST":
            data = request.data
            return {"detail": f"pet {data['petname']} created"}
        return pets

# species

    species = [
            {"id": 1, "speciename": "specie0", "owner": "owner0"},
            {"id": 2, "speciename": "specie1", "owner": "owner1"},
            {"id": 3, "speciename": "specie2", "owner": "owner2"},
        ]

    @app.post("/species/auth")
    def auth_specie():
        data = request.data
        return data

    @app.route("/species/<int:specie_id>", methods=["GET", "PUT", "DELETE"])
    @app.route("/species/", methods=["GET", "POST"])
    def species_endpoint(specie_id=None):
        if specie_id is not None:
            found_specie = None
            for specie in species:
                if specie["id"] == specie_id:
                    found_specie = specie

            if request.method == "PUT":
                return {"detail": f"specie {found_specie['speciename']} modified"}
            if request.method == "DELETE":
                return {"detail": f"specie {found_specie['speciename']} deleted"}

            return found_specie

        if request.method == "POST":
            data = request.data
            return {"detail": f"specie {data['speciename']} created"}
        return species
    
# procedures

    procedures = [
            {"id": 1, "procedurename": "procedure0", "pet": "pet0"},
            {"id": 2, "procedurename": "procedure1", "pet": "pet1"},
            {"id": 3, "procedurename": "procedure2", "pet": "pet2"},
        ]

    @app.post("/procedures/auth")
    def auth_procedure():
        data = request.data
        return data

    @app.route("/procedures/<int:procedure_id>", methods=["GET", "PUT", "DELETE"])
    @app.route("/procedures/", methods=["GET", "POST"])
    def procedures_endpoint(procedure_id=None):
        if procedure_id is not None:
            found_procedure = None
            for procedure in procedures:
                if procedure["id"] == procedure_id:
                    found_procedure = procedure

            if request.method == "PUT":
                return {"detail": f"procedure {found_procedure['procedurename']} modified"}
            if request.method == "DELETE":
                return {"detail": f"procedure {found_procedure['procedurename']} deleted"}

            return found_procedure

        if request.method == "POST":
            data = request.data
            return {"detail": f"procedure {data['procedurename']} created"}
        return procedures



# procedures

    return app