class DataManager:
    def save(self, model):
        print("lamf cac buoc gi do de save model")
        return True


class MongodbManager(DataManager):
    def save(self, model):
        print("Saved model to mongo")
        return True