class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        result = ""
        for document in self.documents:
            result += f"{document}\n"
        return result

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def filtered_category(self, id: int):
        return [category for category in self.categories if category.id == id][0]

    def filtered_topic(self, id: int):
        return [topic for topic in self.topics if topic.id == id][0]

    def filtered_document(self, id: int):
        return [document for document in self.documents if document.id == id][0]

    def edit_category(self, category_id: int, new_name: str):
        self.filtered_category(category_id).name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.filtered_topic(topic_id)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        self.filtered_document(document_id).file_name = new_file_name

    def delete_category(self, category_id: int):
        self.categories.remove(self.filtered_category(category_id))

    def delete_topic(self, topic_id):
        self.topics.remove(self.filtered_topic(topic_id))

    def delete_document(self, document_id):
        self.documents.remove(self.filtered_document(document_id))

    def get_document(self, document_id):
        return self.filtered_document(document_id)
