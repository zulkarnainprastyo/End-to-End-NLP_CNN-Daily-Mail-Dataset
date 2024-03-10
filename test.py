import unittest
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

class TestPipelineStages(unittest.TestCase):

    def test_data_ingestion(self):
        data_ingestion = DataIngestionTrainingPipeline()
        try:
            result = data_ingestion.main()
            self.assertIsNone(result)  # Modify as needed based on your main() function's return type.
        except Exception as e:
            print(f"Exception during data_ingestion: {e}")
            raise

    # Similar modifications for other tests...

if __name__ == '__main__':
    unittest.main()



import unittest
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

class TestDataValidation(unittest.TestCase):

    def test_data_validation(self):
        data_validation = DataValidationTrainingPipeline()
        try:
            result = data_validation.main()
            self.assertIsNone(result)  # Modify as needed based on your main() function's return type.
        except Exception as e:
            print(f"Exception during data_validation: {e}")
            raise

if __name__ == '__main__':
    unittest.main()



import unittest
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline

class TestDataTransformation(unittest.TestCase):

    def test_data_transformation(self):
        data_transformation = DataTransformationTrainingPipeline()
        try:
            result = data_transformation.main()
            self.assertIsNone(result)  # Modify as needed based on your main() function's return type.
        except Exception as e:
            print(f"Exception during data_transformation: {e}")
            raise

if __name__ == '__main__':
    unittest.main()



import unittest
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline

class TestModelTrainer(unittest.TestCase):

    def test_model_trainer(self):
        model_trainer = ModelTrainerTrainingPipeline()
        try:
            result = model_trainer.main()
            self.assertIsNone(result)  # Modify as needed based on your main() function's return type.
        except Exception as e:
            print(f"Exception during model_trainer: {e}")
            raise

if __name__ == '__main__':
    unittest.main()



import unittest
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

class TestModelEvaluation(unittest.TestCase):

    def test_model_evaluation(self):
        model_evaluation = ModelEvaluationTrainingPipeline()
        try:
            result = model_evaluation.main()
            self.assertIsNone(result)  # Modify as needed based on your main() function's return type.
        except Exception as e:
            print(f"Exception during model_evaluation: {e}")
            raise

if __name__ == '__main__':
    unittest.main()
