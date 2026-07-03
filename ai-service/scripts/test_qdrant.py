from app.vectorstore.service import VectorStoreService


def main():

    vector_store = VectorStoreService()

    vector_store.create_collection()

    print(vector_store.health_check())


if __name__ == "__main__":
    main()