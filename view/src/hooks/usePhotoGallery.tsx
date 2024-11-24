import { useState, useEffect } from "react";
import { isPlatform } from "@ionic/react";

import {
  Camera,
  CameraResultType,
  CameraSource,
  // Photo,
} from "@capacitor/camera";
import instance from "../axios";
import axios from "axios";
// import { Filesystem, Directory } from "@capacitor/filesystem";
// import { Preferences } from "@capacitor/preferences";
// import { Capacitor } from "@capacitor/core";

export interface UserPhoto {
  filepath: string;
  webviewPath?: string;
}

export function usePhotoGallery() {
  const [photos, setPhotos] = useState<UserPhoto[]>([]);

  const takePhoto = async () => {
    const photo = await Camera.getPhoto({
      resultType: CameraResultType.Uri,
      source: CameraSource.Camera,
      quality: 100,
    });

    // Convert photo to base64
    const response = await fetch(photo.webPath!);
    const blob = await response.blob();
    const reader = new FileReader();
    reader.readAsDataURL(blob);
    reader.onloadend = async () => {
      const base64data = reader.result as string;

      // Send base64 image to the endpoint
      const result = await instance.post("/check_kannada", {
        image: base64data,
      });

      // Get the annotated image from the response
      const annotatedImageBase64 = result.data.annotated_image;

      // Convert base64 back to image and create a new photo object
      const annotatedImageBlob = await (
        await fetch(annotatedImageBase64)
      ).blob();
      const annotatedImageURL = URL.createObjectURL(annotatedImageBlob);

      const fileName = Date.now() + ".jpeg";
      const newPhotos = [
        {
          filepath: fileName,
          webviewPath: annotatedImageURL,
        },
        ...photos,
      ];
      setPhotos(newPhotos);
    };

    const fileName = Date.now() + ".jpeg";
    const newPhotos = [
      {
        filepath: fileName,
        webviewPath: photo.webPath,
      },
      ...photos,
    ];
    setPhotos(newPhotos);
  };

  return {
    photos,
    takePhoto,
  };
}
