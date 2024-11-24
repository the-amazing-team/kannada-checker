import { IonPage, IonContent, IonLabel } from "@ionic/react";

const Login: React.FC = () => {
  return (
    <IonPage>
      <IonContent fullscreen>
        <div className="flex flex-col items-center justify-center h-full p-6 bg-gray-900 text-white">
          <h1 className="text-3xl font-extrabold mb-4 text-center">
            Login to Kannada Checker
          </h1>
          <div className="w-full max-w-md space-y-4">
            <div>
              <label className="block text-sm font-medium mb-2" htmlFor="email">
                Email
              </label>
              <input
                id="email"
                type="email"
                required
                className="w-full px-4 py-2 border border-gray-600 bg-gray-700 text-white rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition duration-300 ease-in-out"
              />
            </div>
            <div>
              <label
                className="block text-sm font-medium mb-2"
                htmlFor="password"
              >
                Password
              </label>
              <input
                id="password"
                type="password"
                required
                className="w-full px-4 py-2 border border-gray-600 bg-gray-700 text-white rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition duration-300 ease-in-out"
              />
            </div>
            <div className="mt-6">
              <button
                type="submit"
                className="w-full px-4 py-2 bg-indigo-600 text-white rounded-md shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500"
              >
                Login
              </button>
            </div>
            <div className="text-center mt-4">
              <p className="text-sm">
                Don't have an account?{" "}
                <a href="/register" className="text-indigo-500 hover:underline">
                  Register
                </a>
              </p>
            </div>
          </div>
        </div>
      </IonContent>
    </IonPage>
  );
};

export default Login;
