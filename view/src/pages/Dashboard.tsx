import {
  IonPage,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
  IonToast,
} from "@ionic/react";
import ExploreContainer from "../components/ExploreContainer";
import "./Tab1.css";
import FabMenu from "../components/FabMenu";
import { usePhotoGallery } from "../hooks/usePhotoGallery";
import { useState } from "react";
import Gallery from "../components/Gallery";
import instance from "../axios";

const Dashboard: React.FC = () => {
  const { photos, takePhoto } = usePhotoGallery();
  const [showToast, setShowToast] = useState(false);

  const handleTakePhoto = async () => {
    await takePhoto();
    setShowToast(true);
  };

  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>Dashboard</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent fullscreen>
        <IonHeader collapse="condense">
          <IonToolbar>
            <IonTitle size="large">Dashboard</IonTitle>
          </IonToolbar>
        </IonHeader>
        <Gallery
          photos={
            photos.filter((photo) => photo.webviewPath !== undefined) as {
              webviewPath: string;
            }[]
          }
        />
        <IonToast
          isOpen={showToast}
          onDidDismiss={() => setShowToast(false)}
          message="Wait a while the image is being processed"
          duration={2000}
        />
      </IonContent>
      <FabMenu takePhoto={handleTakePhoto} />
    </IonPage>
  );
};

export default Dashboard;
