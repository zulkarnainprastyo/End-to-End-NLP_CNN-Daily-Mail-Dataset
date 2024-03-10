import unittest
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

class TestPipelineStages(unittest.TestCase):

    def test_data_ingestion(self):
        data_ingestion = DataIngestionTrainingPipeline()
        self.assertIsNone(data_ingestion.main())  # Modify as needed based on your main() function's return type.

    def test_data_validation(self):
        data_validation = DataValidationTrainingPipeline()
        self.assertIsNone(data_validation.main())  # Modify as needed based on your main() function's return type.

    def test_data_transformation(self):
        data_transformation = DataTransformationTrainingPipeline()
        self.assertIsNone(data_transformation.main())  # Modify as needed based on your main() function's return type.

    def test_model_trainer(self):
        model_trainer = ModelTrainerTrainingPipeline()
        self.assertIsNone(model_trainer.main())  # Modify as needed based on your main() function's return type.

    def test_model_evaluation(self):
        model_evaluation = ModelEvaluationTrainingPipeline()
        self.assertIsNone(model_evaluation.main())  # Modify as needed based on your main() function's return type.

if __name__ == '__main__':
    unittest.main()
