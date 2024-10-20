class ModelSelection:
    @staticmethod
    def get_model(algorithm: str):
        """Mengembalikan model berdasarkan algoritma yang dipilih"""
        if algorithm == "Random Forest":
            return "random_forest"
        elif algorithm == "Logistic Regression":
            return "logistic_regression"
        else:
            raise ValueError("Algorithm not supported")
