from typing import Any, List, NamedTuple, Optional, Tuple, Union

import cv2
from numpy import float32, int32, ndarray
from yaml import SafeLoader
from yaml import load as yaml_load

from .exceptions import YasodBadInput, YasodModelNotFound
from .models import DetectionModelConfig, YasodConfig


class Detection(NamedTuple):
    class_id: int32
    confidence: float32
    box: ndarray


class Detections(NamedTuple):
    class_ids: ndarray
    confidences: ndarray
    boxes: ndarray


class YasodModel:
    def __init__(self, model_config: Optional[DetectionModelConfig], load_model: bool = True):
        self.model_config = model_config
        self.class_names: Optional[list] = None
        self.model: Optional[Any] = None

        if load_model:
            self.load_model()

    def load_model(self) -> None:
        if not self.model_config:
            raise YasodModelNotFound

        with open(self.model_config.classes_path, "r") as f:
            self.class_names = [class_name.strip() for class_name in f.readlines()]

        self.model = cv2.dnn_DetectionModel(self.model_config.weights_path, self.model_config.config_path)
        self.model.setInputParams(**self.model_config.input_params.dict())

    def detect(self, image: Union[str, ndarray]) -> Tuple[Any, Detections]:
        if isinstance(image, str):
            img = cv2.imread(image)
        elif isinstance(image, ndarray):
            img = cv2.imdecode(image, cv2.IMREAD_COLOR)
        else:
            raise YasodBadInput

        results = self.model.detect(img, **self.model_config.detect_defaults.dict())
        return img, Detections(*results)

    @staticmethod
    def flatten_detections(detections: Detections) -> List[Detection]:
        return [
            Detection(*d)
            for d in zip(
                detections.class_ids.flatten(),
                detections.confidences.flatten(),
                detections.boxes,
            )
        ]

    def label_detection(self, detection: Detection) -> str:
        return self.model_config.draw_defaults.label_format.format(
            self.class_names[detection.class_id + self.model_config.class_offset],
            detection.confidence,
        )

    def draw_results(self, img: Any, detections: Detections, output_img_path: str) -> None:
        for detection in self.flatten_detections(detections):
            label = self.label_detection(detection)
            cv2.rectangle(
                img,
                detection.box,
                self.model_config.draw_defaults.color,
                self.model_config.draw_defaults.thickness,
            )
            cv2.putText(
                img,
                label,
                tuple(detection.box[i] + self.model_config.draw_defaults.offset[i] for i in range(0, 2)),
                self.model_config.draw_defaults.font_const,
                1,
                self.model_config.draw_defaults.color,
                self.model_config.draw_defaults.thickness,
            )
            cv2.imwrite(output_img_path, img)


class Yasod:
    def __init__(self, config_path=None):
        self.config_path = config_path
        if config_path:
            with open(config_path, "r") as file:
                config_dict = yaml_load(file, Loader=SafeLoader)
            self.config = YasodConfig(**config_dict)

        if self.config:
            self.models = {model.name: model for model in self.config.detection_models}
        else:
            self.config = None

    def get_model(
        self,
        name: Optional[str] = None,
        index: Optional[int] = None,
        load_model: bool = True,
    ) -> YasodModel:
        model_config = (
            self.models.get(name) if name else self.config.detection_models[index] if isinstance(index, int) else None
        )

        return YasodModel(model_config, load_model=load_model)

    def get_default_model(self) -> YasodModel:
        return self.get_model(index=0)
