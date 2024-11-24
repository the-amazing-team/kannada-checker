import React, { useState } from "react";
import { IonModal, IonButton, IonContent } from "@ionic/react";

interface Photo {
  webviewPath: string;
}

interface GalleryProps {
  photos: Photo[];
}

function Gallery({ photos }: GalleryProps) {
  const [selectedPhoto, setSelectedPhoto] = useState<Photo | null>(null);

  const openModal = (photo: Photo) => {
    setSelectedPhoto(photo);
  };

  const closeModal = () => {
    setSelectedPhoto(null);
  };

  return (
    <>
      <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4 p-4">
        {photos.map((photo, index) => (
          <img
            key={index}
            src={photo.webviewPath}
            alt={`Photo ${index + 1}`}
            className="w-full h-auto object-cover rounded-lg shadow-md cursor-pointer"
            onClick={() => openModal(photo)}
          />
        ))}
      </div>

      <IonModal
        isOpen={!!selectedPhoto}
        onDidDismiss={closeModal}
        backdropDismiss={true}
      >
        <IonContent>
          {selectedPhoto && (
            <div
              className="flex flex-col items-center justify-center h-full p-4"
              onClick={closeModal}
            >
              <img
                src={selectedPhoto.webviewPath}
                alt="Selected"
                className="w-full h-auto object-cover rounded-lg shadow-md"
                onClick={(e) => e.stopPropagation()}
              />
              {/* <IonButton onClick={closeModal} className="mt-4">
                Close
              </IonButton> */}
            </div>
          )}
        </IonContent>
      </IonModal>
    </>
  );
}

export default Gallery;
