import { IonFab, IonFabButton, IonFabList, IonIcon } from "@ionic/react";
import { add, camera } from "ionicons/icons";
import React from "react";

interface FabMenuProps {
  takePhoto: () => void;
}

function FabMenu({ takePhoto }: FabMenuProps) {
  return (
    <IonFab vertical="bottom" horizontal="end" slot="fixed">
      <IonFabButton>
        <IonIcon icon={add} />
      </IonFabButton>
      <IonFabList side="top">
        <IonFabButton onClick={takePhoto}>
          <IonIcon icon={camera} />
        </IonFabButton>
      </IonFabList>
    </IonFab>
  );
}

export default FabMenu;
