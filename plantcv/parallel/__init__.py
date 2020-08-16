import os
import sys
import json
from copy import deepcopy
from plantcv.parallel.parsers import metadata_parser
from plantcv.parallel.parsers import check_date_range
from plantcv.parallel.job_builder import job_builder
from plantcv.parallel.process_results import process_results
from plantcv.parallel.multiprocess import multiprocess

__all__ = ["metadata_parser", "job_builder", "process_results", "multiprocess", "check_date_range", "WorkflowConfig"]


class WorkflowConfig:
    def __init__(self):
        self.input_dir = ""
        self.json = ""
        self.filename_metadata = []
        self.workflow = ""
        self.output_dir = "./output_images"
        self.tmp_dir = None
        self.processes = 1
        self.start_date = 1
        self.end_date = None
        self.imgformat = "png"
        self.delimiter = "_"
        self.metadata_filters = {}
        self.timestampformat = "%Y-%m-%d %H:%M:%S.%f"
        self.writeimg = False
        self.other_args = []
        self.coprocess = None
        self.metadata_terms = {
                # Camera settings
                "camera": {
                    "label": "camera identifier",
                    "datatype": "<class 'str'>",
                    "value": "none"
                },
                "imgtype": {
                    "label": "image type",
                    "datatype": "<class 'str'>",
                    "value": "none"
                },
                "zoom": {
                    "label": "camera zoom setting",
                    "datatype": "<class 'str'>",
                    "value": "none"
                },
                "exposure": {
                    "label": "camera exposure setting",
                    "datatype": "<class 'str'>",
                    "value": "none"
                },
                "gain": {
                    "label": "camera gain setting",
                    "datatype": "<class 'str'>",
                    "value": "none"
                },
                "frame": {
                    "label": "image series frame identifier",
                    "datatype": "<class 'str'>",
                    "value": "none"
                },
                "lifter": {
                    "label": "imaging platform height setting",
                    "datatype": "<class 'str'>",
                    "value": "none"
                },
                # Date-Time
                "timestamp": {
                    "label": "datetime of image",
                    "datatype": "<class 'datetime.datetime'>",
                    "value": None
                },
                # Sample attributes
                "id": {
                    "label": "image identifier",
                    "datatype": "<class 'str'>",
                    "value": "none"
                },
                "plantbarcode": {
                    "label": "plant barcode identifier",
                    "datatype": "<class 'str'>",
                    "value": "none"
                },
                "treatment": {
                    "label": "treatment identifier",
                    "datatype": "<class 'str'>",
                    "value": "none"
                },
                "cartag": {
                    "label": "plant carrier identifier",
                    "datatype": "<class 'str'>",
                    "value": "none"
                },
                # Experiment attributes
                "measurementlabel": {
                    "label": "experiment identifier",
                    "datatype": "<class 'str'>",
                    "value": "none"
                },
                # Other
                "other": {
                    "label": "other identifier",
                    "datatype": "<class 'str'>",
                    "value": "none"
                }
            }

    # Save configuration to a file
    def save_config(self, config_file):
        """Save configuration to a file.

        Input variables:
        config_file = Filename to write configuration to (text/JSON)

        :param config_file: str
        """
        # Open the file for writing
        with open(config_file, "w") as fp:
            # Save the data in JSON format with indentation
            json.dump(obj=vars(self), fp=fp, indent=4)

    # Import a configuration from a file
    def import_config(self, config_file):
        """Import a configuration file.

        Input variables:
        config_file = Configuration file to import

        :param config_file: str
        """
        # Open the file for reading
        with open(config_file, "r") as fp:
            # Import the JSON configuration data
            config = json.load(fp)
            for key, value in config.items():
                setattr(self, key, value)

    # Validation checks on current config
    def validate_config(self):
        """Validation checks on current configuration.
        """
        checks = [True]
        # Validate input directory
        if not os.path.exists(self.input_dir):
            print(f"Error: input directory (input_dir) is required and {self.input_dir} does not exist.",
                  file=sys.stderr)
            checks.append(False)
        # Validate JSON file
        if self.json == "":
            print("Error: an output JSON file (json) is required but is currently undefined.", file=sys.stderr)
            checks.append(False)
        # Validate filename metadata
        if len(self.filename_metadata) == 0:
            print("Error: a list of filename metadata terms (filename_metadata) is required but is currently undefined",
                  file=sys.stderr)
            checks.append(False)
        else:
            # Are the user-defined metadata valid?
            for term in self.filename_metadata:
                if term not in self.metadata_terms:
                    print(f"Error: the term {term} in filename_metadata is not a currently supported metadata type.",
                          file=sys.stderr)
                    checks.append(False)
        # Validate workflow script
        if not os.path.exists(self.workflow):
            print(f"Error: PlantCV workflow script (workflow) is required and {self.workflow} does not exist.",
                  file=sys.stderr)
            checks.append(False)
        return all(checks)
