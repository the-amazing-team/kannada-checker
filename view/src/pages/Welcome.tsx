import { IonContent, IonPage } from "@ionic/react";

const Welcome: React.FC = () => {
  return (
    <IonPage>
      <IonContent fullscreen>
        <div className="flex flex-col items-center justify-between h-full p-6 bg-black text-white">
          <div className="flex flex-col items-center justify-center flex-grow">
            <h1 className="text-3xl font-extrabold mb-4 text-center">
              Welcome to Kannada Checker
            </h1>
            <p className="text-center mb-8 text-base max-w-md">
              Upload an image to check the percentage of Kannada text in it. Our
              advanced AI will analyze the image and provide you with accurate
              results.
            </p>
          </div>
          <div className="mt-auto w-full">
            <button className="bg-white text-black w-full px-8 py-3 rounded-full shadow-lg hover:bg-gray-200 transition duration-300 mb-4">
              Get Started
            </button>
          </div>
        </div>
      </IonContent>
    </IonPage>
  );
};

export default Welcome;
