import pytest
import os
import pickle as pkl
import numpy as np
import matplotlib

# Disable plotting
matplotlib.use("Template")


class TestData:
    def __init__(self):
        """Initialize simple variables."""
        # Test data directory
        self.datadir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testdata")
        # Flat image directory
        self.snapshot_dir = os.path.join(self.datadir, "snapshot_dir")
        # RGB image
        self.small_rgb_img = os.path.join(self.datadir, "setaria_small_plant_rgb.png")
        # Binary mask for RGB image
        self.small_bin_img = os.path.join(self.datadir, "setaria_small_plant_mask.png")
        # Gray image
        self.small_gray_img = os.path.join(self.datadir, "setaria_small_plant_gray.png")
        # Contours file
        self.small_contours_file = os.path.join(self.datadir, "setaria_small_plant_contours.npz")
        # Composed contours file
        self.small_composed_contours_file = os.path.join(self.datadir, "setaria_small_plant_composed_contours.npz")
        # PlantCV Spectral_data object
        self.hsi_file = os.path.join(self.datadir, "hsi.pkl")
        # Binary mask for HSI
        self.hsi_mask_file = os.path.join(self.datadir, "hsi_mask.png")
        # Outputs results file - JSON
        self.outputs_results_json = os.path.join(self.datadir, "outputs_results.json")
        # Outputs results file - CSV
        self.outputs_results_csv = os.path.join(self.datadir, "outputs_results.csv")
        # RGBA image
        # Image from http://www.libpng.org/pub/png/png-OwlAlpha.html
        # This image may be used, edited and reproduced freely.
        self.rgba_img = os.path.join(self.datadir, "owl_rgba_img.png")
        # ENVI hyperspectral data
        self.envi_bil_file = os.path.join(self.datadir, "darkReference")
        # Thermal image
        self.thermal_img = os.path.join(self.datadir, "FLIR2600.csv")
        # Thermal image data
        self.thermal_obj_file = os.path.join(self.datadir, "thermal_img.npz")
        # Thermal image mask
        self.thermal_mask = os.path.join(self.datadir, "thermal_img_mask.png")
        # Bayer image
        self.bayer_img = os.path.join(self.datadir, "bayer_img.png")
        # Naive Bayes trained model file
        self.nb_trained_model = os.path.join(self.datadir, "naive_bayes_pdfs.txt")
        # Naive Bayes bad model file
        self.nb_bad_model = os.path.join(self.datadir, "naive_bayes_pdfs_bad.txt")
        # acute example results
        self.acute_results = np.asarray([[[119, 285]], [[151, 280]], [[168, 267]], [[168, 262]], [[171, 261]], [[224, 269]],
                                         [[246, 271]], [[260, 277]], [[141, 248]], [[183, 194]], [[188, 237]], [[173, 240]],
                                         [[186, 260]], [[147, 244]], [[163, 246]], [[173, 268]], [[170, 272]], [[151, 320]],
                                         [[195, 289]], [[228, 272]], [[210, 272]], [[209, 247]], [[210, 232]]])
        # Fmin image
        self.fmin = os.path.join(self.datadir, "FLUO_TV_min.png")
        # Fmax image
        self.fmax = os.path.join(self.datadir, "FLUO_TV_max.png")
        # Mask image
        self.ps_mask = os.path.join(self.datadir, "FLUO_TV_MASK.png")
        # Multi-plant RGB image
        self.multi_rgb_img = os.path.join(self.datadir, "brassica_multi_rgb_img.jpg")
        # Multi-plant contours file
        self.multi_contours_file = os.path.join(self.datadir, "brassica_multi_contours.npz")
        # Two plants binary mask
        self.multi_bin_img = os.path.join(self.datadir, "brassica_2plants_bin_img.png")
        # Clustered contours names file
        self.cluster_names = os.path.join(self.datadir, "cluster_names.txt")
        # Clustered contours names file with too many labels
        self.cluster_names_too_many = os.path.join(self.datadir, "cluster_names_too_many.txt")

    def load_hsi(self, pkl_file):
        """Load PlantCV Spectral_data pickled object."""
        with open(pkl_file, "rb") as fp:
            return pkl.load(fp)

    def load_contours(self, npz_file):
        """Load data saved in a NumPy .npz file."""
        data = np.load(npz_file, encoding="latin1", allow_pickle=True)
        return data['contours'], data['hierarchy']

    def load_composed_contours(self, npz_file):
        """Load data saved in a NumPy .npz file."""
        data = np.load(npz_file, encoding="latin1")
        return data['contour']

    def load_npz(self, npz_file):
        """Load data saved in a NumPy .npz file."""
        data = np.load(npz_file, encoding="latin1")
        return data['arr_0']


@pytest.fixture(scope="session")
def test_data():
    return TestData()
