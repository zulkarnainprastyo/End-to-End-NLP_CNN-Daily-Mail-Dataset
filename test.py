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
