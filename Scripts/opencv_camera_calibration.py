__author__ = 'zigaso'

''' capital C Camera class, represents, you guessed it, a camera '''

import cv2
import numpy as np
import pickle

class Camera(object):
    """
    Camera calibration based on planar checkerboard image
    - get the image from https://www.mrpt.org/downloads/camera-calibration-checker-board_9x7.pdf
    - print the thing and make sure to measure the number (6x9) and size of squares
    - update the init function accordingly

    Camera GUI allow the user to control camera exposure using slider. This has to be setup wisely.

    Other GUI controls are via keyboard:
        a: acquire one image
        c: try to calibrate
        t: toggle camera conrols
        r: remove previous frame
        ESC: exit

    Allows on to calibrate a single camera or a stereo pair. Typical use cases for three modes:
        0: show camera frame
        1: run single camera calibration gui
        2: run stereo camera pair gui
        3: load camera intrinsics from file and print
    are shown at the end of the file. To calibrate camera simply use the command:

    python opencv_camera_calibration.py 1

    Good luck and always remember to have fun!
    """
    def __init__(
            self,
            name='neither left nor right',
            device_number=0,
            exposure=None,
            w=1280,
            h=1024,
            checkerboard_rows=7,
            checkerboard_cols=9,
            checkerboard_square_size_cm=2.54):
        self.extrinsics_present = False
        self.name = name
        self.cap = cv2.VideoCapture(device_number)
        # NOTE: commented out
        if exposure is not None:
            self.exposure = exposure
            self.cap.set(cv2.CAP_PROP_EXPOSURE, self.exposure)
        else:
            self.exposure = - self.cap.get(cv2.CAP_PROP_EXPOSURE)
        # self.cap.set(cv2.CAP_PROP_XI_AUTO_WB,-1.0)

        # utility windows properties
        self.controls_window_name = 'CONTROLS' + name
        self.controls_window_visible = False
        self.show_frame_window_name = name
        self.show_window_name = name

        # frame geometry
        self.w = w
        self.h = h
        self.size = (w, h)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

        # overlay text properties
        self.overlay_text = ['ESC: close window']  # a list of strings, must be a list even if has only one item
        self.overlay_text_size = 1
        self.overlay_text_color = (0, 255, 255)
        self.overlay_text_line_spacing = 30

        # calibration mode constants
        self.calibration_mode_window_name = 'calibration mode'
        self.chessboard_window_name = 'detected chessboard'

        # calibration pattern properties (points where black squares' edges meet)
        self.rows = checkerboard_rows                   # n-1
        self.columns = checkerboard_cols                # m-1
        self.square_size = checkerboard_square_size_cm  # in cm

        # Calibration properties
        self.is_calibrated = False
        self.cameraMatrix = None
        self.distCoeffs = None

        # Try to load previously saved calibration parameters
        if self.load_intrinsics():
            print("intrinsic calibration parameters for camera " + self.name + ' were loaded successfully \n')
            self.is_calibrated = True

        # Try to load previously saved calibration parameters
        if self.load_extrinsics():
            print("extrinsic calibration parameters for camera " + self.name + ' were loaded successfully \n')
            self.extrinsics_present = True
        self._calibration_init()

    ###################### CONTROLS ####################################
    def toggle_controls(self):
        if self.controls_window_visible:
            self.hide_controls()
        else:
            self.show_controls()

    def show_controls(self):
        cv2.namedWindow(self.controls_window_name)
        # NOTE: commented out
        cv2.createTrackbar(
            "Exposure",
            self.controls_window_name,
            int(-self.cap.get(cv2.CAP_PROP_EXPOSURE)),
            11,
            lambda x: self.cap.set(cv2.CAP_PROP_EXPOSURE, -x)
        )
        self.controls_window_visible = True

    def hide_controls(self):
        cv2.destroyWindow(self.controls_window_name)
        self.controls_window_visible = False

    ################## UTILITIES AND WRAPPERS ###########################
    def read(self):
        _, self.im = self.cap.read()
        return self.im

    def grab(self):
        return self.cap.grab()

    def retrieve(self):
        _, self.im =  self.cap.retrieve()
        return _, self.im

    def show_frame(self):
        _, im = self.cap.read()
        cv2.imshow(self.show_frame_window_name, im)
        ch = cv2.waitKey(1)
        return ch

    def close(self):
        self.cap.release()

    def show(self, window_name=False):
        if not window_name:
            window_name = self.show_window_name
        cv2.imshow(self.show_window_name, self.im)

    ############################ CALIBRATION ################################
    def _calibration_init(self):
        # prepare the data structures
        self.calibration_points = []  # a list for holding detected corners
        # preparing world corner coords
        pattern_size = (self.rows, self.columns)
        corner_coordinates = np.zeros((np.prod(pattern_size), 3), np.float32)
        corner_coordinates[:, :2] = np.indices(pattern_size).T.reshape(-1, 2)
        corner_coordinates = corner_coordinates * self.square_size
        self.corner_coordinates = corner_coordinates
        self.world_points = []

    def calibrate_gui(self):
        # prepare windows
        cv2.namedWindow(self.calibration_mode_window_name)
        cv2.namedWindow(self.chessboard_window_name)

        # add text
        self.overlay_text = [
            'a: acquire one image',
            'c: try to calibrate',
            't: toggle camera conrols',
            'r: remove previous frame',
            'ESC: exit',
            '0 images acquired'
        ]

        switch_case = {
            ord('a'): self.calibration_append_and_show,
            ord('c'): self.calibrate,
            ord('t'): self.toggle_controls,
            ord('r'): self.remove_and_show,
        }

        ch = 0
        while ch != 27:
            self.read()
            im_with_overlay = self.add_overlay_text()
            cv2.imshow('calibration mode', im_with_overlay)
            ch = cv2.waitKey(1)  # & 0xFF
            # switch-case, see beginning of this method for cases
            func = switch_case.get(ch, lambda: "nothing")
            func()

    def return_chessboard_corners_image(self):
        temp = self.im.copy()
        cv2.drawChessboardCorners(
            temp,
            (self.rows, self.columns),
            self.calibration_points[-1].reshape(-1, 1, 2),
            True
        )
        return temp

    def calibration_append_and_show(self):
        if self.calibration_append():
            # show them corners
            cv2.drawChessboardCorners(
                self.im,
                (self.rows, self.columns),
                self.calibration_points[-1].reshape(-1, 1, 2),
                True
            )
            cv2.imshow(self.chessboard_window_name,self.im)

            # Increment the counter in the overlay text
            current_number_of_images = int(self.overlay_text[5].split()[0])
            assert current_number_of_images == len(self.calibration_points)-1
            # a one-liner to replace the count
            self.overlay_text[5] = ' '.join([str(len(self.calibration_points))] + self.overlay_text[5].split()[1:3])

    def calibration_append(self, im = False):
        """Find subpixel chessboard corners in image."""
        if im is False:
            im  = self.im.copy()
        temp = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(
            temp,
            (self.rows, self.columns)
        )
        if not ret:
            return False
        else:
            cv2.cornerSubPix(temp, corners, (5, 5), (-1, -1),
                             (cv2.TERM_CRITERIA_MAX_ITER + cv2.TERM_CRITERIA_EPS,
                              30, 0.01))
            # APPEND
            # reshapeth!, adopted from StereoVision module, removes a singleton dim (LIKE MATLAB SQUEEZE)
            self.calibration_points.append(corners.reshape(-1, 2))
            self.world_points.append(self.corner_coordinates)
            return True

    def remove_calibration_frame(self):
        if len(self.calibration_points) > 0 and len(self.world_points) > 0:
            del self.calibration_points[-1]
            del self.world_points[-1]

    def remove_and_show(self):
        self.remove_calibration_frame()
        cv2.imshow(
            self.chessboard_window_name,
            self.add_overlay_text(self.im.copy(), text=['Calibration frame removed'])
        )
        # a one-liner to replace the count
        self.overlay_text[5] = ' '.join([str(len(self.calibration_points))] + self.overlay_text[5].split()[1:3])

    def calibrate(self):
        if len(self.world_points)==0 or len(self.calibration_points)==0:
            print('Cannot calibrate from 0 images, you must acquire a few checkerboard images!')
            return -1

        cameraMatrix = np.array([[self.w, 0, self.w/2], [0, self.w, self.h/2], [0, 0, 1]])
        dist_coef = np.array([0, 0, 0, 0, 0])

        retval, cameraMatrix, distCoeffs, rvecs, tvecs = cv2.calibrateCamera(
            np.array(self.world_points),
            np.array(self.calibration_points),
            (self.w, self.h),
            None,
            None
        )
        print('rms:', retval)
        print('\n cameraMatrix:', cameraMatrix)
        print('\n distortion coeffs:', distCoeffs)

        self.cameraMatrix = cameraMatrix
        self.distCoeffs = distCoeffs
        self.is_calibrated = True
        self.save_intrinsics()
        return retval

    def save_intrinsics(self):
        to_save = {'cameraMatrix': self.cameraMatrix,
                   'distCoeffs': self.distCoeffs,
                   }
        pickle.dumps(to_save)
        with open(self.name + '.intrinsics', 'wb') as f:
            pickle.dump(to_save, f)

    def load_intrinsics(self, filename=False):
        if not filename:
            filename = self.name + '.intrinsics'
        try:
            with open(filename, 'rb') as f:
                temp_dic = pickle.load(f)
                self.cameraMatrix = temp_dic['cameraMatrix']
                self.distCoeffs = temp_dic['distCoeffs']
                return True
        except EnvironmentError:
            return False

    def add_overlay_text(self, im=False, text=False):
        if im is False:
            im = self.im.copy()  # if second argument was not specified
        if text is False:
            text = self.overlay_text
        nlines = len(text)  # how many line to output
        for i in range(nlines):
            cv2.putText(
                im,
                text[i],
                (0, (i+1)*self.overlay_text_line_spacing),
                cv2.FONT_HERSHEY_COMPLEX,
                int(self.overlay_text_size),
                self.overlay_text_color
            )

        return im

    def undistort_points(self,point_coordinates_uv,R = None):
        ## THE WAY IT IS NOW THIS FUNCTION IS ONLY USABLE AFTER EXTRINSIC CALIBRATION
        # import pdb
        # pdb.set_trace()
        p = cv2.undistortPoints(np.expand_dims(point_coordinates_uv,0).astype(np.float32),
                                self.cameraMatrix,self.distCoeffs, P = self.P, R = self.R)
        # TODO: IMPORTANT: DOUBLE CHECK THAT THE SLICING IS IN THE RIGHT DIRECTION
        return p

    def save_extrinsics(self, filename = None):
        if not self.extrinsics_present:
            print('Camera warning: could not save extrinsics - nothing to save')
            return
        if filename is None:
            filename = '%s.extrinsics' % self.name

        to_save = {
            'P': self.P,
            'R': self.R,
            'validPixROI': self.validPixROI
        }
        try:
            with open(filename, 'wb') as f:
                pickle.dump(to_save, f)
        except EnvironmentError: # e.g. cant open file
            print('Camera warning: could not save extrinsics due to IO error')


    def load_extrinsics(self,filename = None):
        if filename is None:
            filename = '%s.extrinsics' % self.name

        try:
            with open(filename, 'rb') as f:
                to_load = pickle.load(f)
                for key in to_load.keys():
                    self.__setattr__(key,  to_load[key])
                return True
        except EnvironmentError:
            return False


################### TEST CLAUSES ###########################
if __name__ == '__main__':
    test_to_run = [0]
    import sys
    if len(sys.argv):
        test_to_run = [int(x) for x in sys.argv[1:]]

    cam = Camera('test camera', 0) # here, zero is camera id (could be different for your setup)
    cam.show_controls()
    # TEST 0
    if 0 in test_to_run:
        FLAG_TERM = 1
        while FLAG_TERM != 27:
            FLAG_TERM = cam.show_frame()
            if FLAG_TERM == ord('c'):
                cam.toggle_controls()

    # TEST 1
    if 1 in test_to_run:
        cam.calibrate_gui()

    # TEST 2 - two cams
    if 2 in test_to_run:
        FLAG_TERM = 1
        cam1 = Camera('another camera', 1)
        cam1.show_controls()
        while FLAG_TERM != 27:
            FLAG_TERM = cam.show_frame()
            cam1.show_frame()
            if FLAG_TERM == ord('c'):
                cam.toggle_controls()
            if FLAG_TERM == ord('d'):
                cam1.toggle_controls()
    # TEST 3
    if 3 in test_to_run:
        cam.load_intrinsics()
        print(cam.cameraMatrix, '\n', cam.distCoeffs)
    # cleanup
    cam.close()
