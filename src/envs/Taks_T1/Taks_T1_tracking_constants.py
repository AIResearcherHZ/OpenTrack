# Copyright 2025 DeepMind Technologies Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Constants for Taks_T1."""

from pathlib import Path
import numpy as np

ROOT_PATH = Path(__file__).parent.parent.parent.parent / "data" / "xmls" / "Taks_T1"
FEET_ONLY_FLAT_TERRAIN_XML = ROOT_PATH / "scene_mjx_feetonly_flat_terrain.xml"
FEET_ONLY_ROUGH_TERRAIN_XML = ROOT_PATH / "scene_mjx_feetonly_rough_terrain.xml"

# Taks_T1 has 32 joints: 12 leg + 3 waist + 14 arm + 3 neck
NUM_JOINT = 32


def task_to_xml(task_name: str) -> Path:
    return {
        "flat_terrain": FEET_ONLY_FLAT_TERRAIN_XML,
        "rough_terrain": FEET_ONLY_ROUGH_TERRAIN_XML,
    }[task_name]


FEET_SITES = [
    "left_foot",
    "right_foot",
]

FEET_ALL_SITES = [
    "left_foot",
    "right_foot",
    "left_foot_top",
    "right_foot_top",
]

HAND_SITES = [
    "left_palm",
    "right_palm",
]

LEFT_FEET_GEOMS = ["left_foot"]
RIGHT_FEET_GEOMS = ["right_foot"]
FEET_GEOMS = LEFT_FEET_GEOMS + RIGHT_FEET_GEOMS

ROOT_BODY = "torso_link"

GRAVITY_SENSOR = "upvector"
GLOBAL_LINVEL_SENSOR = "global_linvel"
GLOBAL_ANGVEL_SENSOR = "global_angvel"
LOCAL_LINVEL_SENSOR = "local_linvel"
ACCELEROMETER_SENSOR = "accelerometer"
GYRO_SENSOR = "gyro"

RESTRICTED_JOINT_RANGE = (
    # Left leg.
    (-2.5307, 2.8798),   # left_hip_pitch
    (-0.5236, 2.9671),   # left_hip_roll
    (-2.7576, 2.7576),   # left_hip_yaw
    (-0.087267, 2.8798), # left_knee
    (-0.87267, 0.5236),  # left_ankle_pitch
    (-0.2618, 0.2618),   # left_ankle_roll
    # Right leg.
    (-2.5307, 2.8798),   # right_hip_pitch
    (-2.9671, 0.5236),   # right_hip_roll
    (-2.7576, 2.7576),   # right_hip_yaw
    (-0.087267, 2.8798), # right_knee
    (-0.87267, 0.5236),  # right_ankle_pitch
    (-0.2618, 0.2618),   # right_ankle_roll
    # Waist.
    (-2.618, 2.618),     # waist_yaw
    (-0.52, 0.52),       # waist_roll
    (-0.52, 0.52),       # waist_pitch
    # Left arm.
    (-3.0, 2.0),         # left_shoulder_pitch
    (-0.2, 2.2515),      # left_shoulder_roll
    (-2.58, 2.58),       # left_shoulder_yaw
    (-0.7, 1.57),        # left_elbow
    (-2.67, 2.67),       # left_wrist_roll
    (-0.9, 0.9),         # left_wrist_yaw
    (-0.9, 0.9),         # left_wrist_pitch
    # Right arm.
    (-2.0, 2.0),         # right_shoulder_pitch
    (-2.2515, 0.2),      # right_shoulder_roll
    (-2.58, 2.58),       # right_shoulder_yaw
    (-0.7, 1.57),        # right_elbow
    (-2.67, 2.67),       # right_wrist_roll
    (-0.9, 0.9),         # right_wrist_yaw
    (-0.9, 0.9),         # right_wrist_pitch
    # Neck.
    (-1.57, 1.57),       # neck_yaw
    (-0.873, 0.873),     # neck_roll
    (-0.873, 0.873),     # neck_pitch
)

DOF_VEL_LIMITS = [
    # Left leg
    32.0, 32.0, 32.0, 20.0, 37.0, 37.0,
    # Right leg
    32.0, 32.0, 32.0, 20.0, 37.0, 37.0,
    # Waist
    32.0, 37.0, 37.0,
    # Left arm
    37.0, 37.0, 37.0, 37.0, 37.0, 37.0, 37.0,
    # Right arm
    37.0, 37.0, 37.0, 37.0, 37.0, 37.0, 37.0,
    # Neck
    20.0, 20.0, 20.0,
]

ACTION_JOINT_NAMES = [
    # left leg
    "left_hip_pitch_joint",
    "left_hip_roll_joint",
    "left_hip_yaw_joint",
    "left_knee_joint",
    "left_ankle_pitch_joint",
    "left_ankle_roll_joint",
    # right leg
    "right_hip_pitch_joint",
    "right_hip_roll_joint",
    "right_hip_yaw_joint",
    "right_knee_joint",
    "right_ankle_pitch_joint",
    "right_ankle_roll_joint",
    # -------------- tracking only --------------
    # waist
    "waist_yaw_joint",
    "waist_roll_joint",
    "waist_pitch_joint",
    # left arm
    "left_shoulder_pitch_joint",
    "left_shoulder_roll_joint",
    "left_shoulder_yaw_joint",
    "left_elbow_joint",
    "left_wrist_roll_joint",
    "left_wrist_yaw_joint",
    "left_wrist_pitch_joint",
    # right arm
    "right_shoulder_pitch_joint",
    "right_shoulder_roll_joint",
    "right_shoulder_yaw_joint",
    "right_elbow_joint",
    "right_wrist_roll_joint",
    "right_wrist_yaw_joint",
    "right_wrist_pitch_joint",
    # neck
    "neck_yaw_joint",
    "neck_roll_joint",
    "neck_pitch_joint",
]

OBS_JOINT_NAMES = [
    # left leg
    "left_hip_pitch_joint",
    "left_hip_roll_joint",
    "left_hip_yaw_joint",
    "left_knee_joint",
    "left_ankle_pitch_joint",
    "left_ankle_roll_joint",
    # right leg
    "right_hip_pitch_joint",
    "right_hip_roll_joint",
    "right_hip_yaw_joint",
    "right_knee_joint",
    "right_ankle_pitch_joint",
    "right_ankle_roll_joint",
    # waist
    "waist_yaw_joint",
    "waist_roll_joint",
    "waist_pitch_joint",
    # left arm
    "left_shoulder_pitch_joint",
    "left_shoulder_roll_joint",
    "left_shoulder_yaw_joint",
    "left_elbow_joint",
    "left_wrist_roll_joint",
    "left_wrist_yaw_joint",
    "left_wrist_pitch_joint",
    # right arm
    "right_shoulder_pitch_joint",
    "right_shoulder_roll_joint",
    "right_shoulder_yaw_joint",
    "right_elbow_joint",
    "right_wrist_roll_joint",
    "right_wrist_yaw_joint",
    "right_wrist_pitch_joint",
    # neck
    "neck_yaw_joint",
    "neck_roll_joint",
    "neck_pitch_joint",
]

# fmt: off
TORQUE_LIMIT = np.array([
    # Left leg
    120., 97., 97., 120., 27., 27.,
    # Right leg
    120., 97., 97., 120., 27., 27.,
    # Waist
    97., 97., 97.,
    # Left arm
    27., 27., 27., 27., 7., 7., 7.,
    # Right arm
    27., 27., 27., 27., 7., 7., 7.,
    # Neck
    3., 3., 3.,
])

DEFAULT_QPOS = np.float32([
    0, 0, 0.793,
    1, 0, 0, 0,
    # Left leg
    -0.1, 0, 0, 0.3, -0.2, 0,
    # Right leg
    -0.1, 0, 0, 0.3, -0.2, 0,
    # Waist
    0, 0, 0,
    # Left arm
    0.2, 0.2, 0, 0.5, 0, 0, 0,
    # Right arm
    0.2, -0.2, 0, 0.5, 0, 0, 0,
    # Neck
    0, 0, 0,
])

KPs = np.float32([
    # Left leg
    100, 100, 100, 200, 80, 20,
    # Right leg
    100, 100, 100, 200, 80, 20,
    # Waist
    300, 300, 300,
    # Left arm
    90, 60, 20, 60, 20, 20, 20,
    # Right arm
    90, 60, 20, 60, 20, 20, 20,
    # Neck
    20, 20, 20,
])

KDs = np.float32([
    # Left leg
    2, 2, 2, 4, 2, 1,
    # Right leg
    2, 2, 2, 4, 2, 1,
    # Waist
    10, 10, 10,
    # Left arm
    2, 2, 1, 1, 1, 1, 1,
    # Right arm
    2, 2, 1, 1, 1, 1, 1,
    # Neck
    1, 1, 1,
])

UPPER_BODY_LINKs = [
    "left_shoulder_pitch_link",
    "left_shoulder_roll_link",
    "left_shoulder_yaw_link",
    "left_elbow_link",
    "left_wrist_roll_link",
    "left_wrist_yaw_link",
    "left_wrist_pitch_link",
    "right_shoulder_pitch_link",
    "right_shoulder_roll_link",
    "right_shoulder_yaw_link",
    "right_elbow_link",
    "right_wrist_roll_link",
    "right_wrist_yaw_link",
    "right_wrist_pitch_link",
    "neck_yaw_link",
    "neck_roll_link",
    "neck_pitch_link",
]

LOWER_BODY_LINKs = [
    "pelvis",
    "left_hip_pitch_link",
    "left_hip_roll_link",
    "left_hip_yaw_link",
    "left_knee_link",
    "left_ankle_pitch_link",
    "left_ankle_roll_link",
    "right_hip_pitch_link",
    "right_hip_roll_link",
    "right_hip_yaw_link",
    "right_knee_link",
    "right_ankle_pitch_link",
    "right_ankle_roll_link",
    "waist_yaw_link",
    "waist_roll_link",
    "torso_link",
]

UPPER_BODY_JOINTs = [
    # left arm
    "left_shoulder_pitch_joint",
    "left_shoulder_roll_joint",
    "left_shoulder_yaw_joint",
    "left_elbow_joint",
    "left_wrist_roll_joint",
    "left_wrist_yaw_joint",
    "left_wrist_pitch_joint",
    # right arm
    "right_shoulder_pitch_joint",
    "right_shoulder_roll_joint",
    "right_shoulder_yaw_joint",
    "right_elbow_joint",
    "right_wrist_roll_joint",
    "right_wrist_yaw_joint",
    "right_wrist_pitch_joint",
    # neck
    "neck_yaw_joint",
    "neck_roll_joint",
    "neck_pitch_joint",
]


FEET_LINKs = ["left_ankle_roll_link", "right_ankle_roll_link"]

SHOULDER_LINKs = ["right_shoulder_pitch_link", "left_shoulder_pitch_link"]


LAFAN1_DATASETS = [
    "dance1_subject1",
    "dance1_subject2",
    "dance1_subject3",
    "dance2_subject1",
    "dance2_subject2",
    "dance2_subject3",
    "dance2_subject4",
    "dance2_subject5",
    "fallAndGetUp1_subject1",
    "fallAndGetUp1_subject5",
    "fallAndGetUp2_subject2",
    "fallAndGetUp3_subject1",
    "fight1_subject2",
    "fight1_subject3",
    "fight1_subject5",
    "fightAndSports1_subject1",
    "fightAndSports1_subject4",
    "jumps1_subject1",
    "jumps1_subject2",
    "jumps1_subject5",
    "run1_subject2",
    "run1_subject5",
    "run2_subject1",
    "run2_subject4",
    "sprint1_subject2",
    "sprint1_subject4",
    "walk1_subject1",
    "walk1_subject2",
    "walk1_subject5",
    "walk2_subject1",
    "walk2_subject4",
    "walk3_subject1",
    "walk3_subject2",
    "walk3_subject3",
    "walk3_subject4",
    "walk3_subject5",
    "walk4_subject1",
]
