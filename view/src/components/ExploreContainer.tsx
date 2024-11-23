import React from "react";
import Webcam from "react-webcam";
import "./ExploreContainer.css";
import { usePhotoGallery } from "../hooks/usePhotoGallery";
import { IonCol, IonImg } from "@ionic/react";

interface ContainerProps {
  name: string;
}

const ExploreContainer: React.FC<ContainerProps> = ({ name }) => {
  const { photos, takePhoto } = usePhotoGallery();

  return (
    <div className="container">
      <strong>{name}</strong>
      <p>
        Explore{" "}
        <a
          target="_blank"
          rel="noopener noreferrer"
          href="https://ionicframework.com/docs/components"
        >
          UI Components
        </a>
        {photos.map((photo, index) => (
          <IonCol size="6" key={photo.filepath}>
            <IonImg src={photo.webviewPath} />
          </IonCol>
        ))}
        <button onClick={takePhoto}>Take Photo</button>
      </p>
    </div>
  );
};

export default ExploreContainer;
