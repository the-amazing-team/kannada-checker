import { IonPage, IonContent, IonLabel } from "@ionic/react";

const Register: React.FC = () => {
  return (
    <IonPage>
      <IonContent fullscreen>
        <div className="flex flex-col items-center justify-center h-full p-6 bg-gray-900 text-white">
          <h1 className="text-3xl font-extrabold mb-4 text-center">
            Register for Kannada Checker
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
            <div>
              <label
                className="block text-sm font-medium mb-2"
                htmlFor="confirm-password"
              >
                Confirm Password
              </label>
              <input
                id="confirm-password"
                type="password"
                required
                className="w-full px-4 py-2 border border-gray-600 bg-gray-700 text-white rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition duration-300 ease-in-out"
              />
            </div>
            <div>
              <button
                type="submit"
                className="w-full px-4 py-2 bg-indigo-600 text-white rounded-md shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 transition duration-300 ease-in-out"
              >
                Register
              </button>
            </div>
            <div className="text-center">
              <p className="text-sm">
                Already have an account?{" "}
                <a href="/login" className="text-indigo-500 hover:underline">
                  Login
                </a>
              </p>
            </div>
          </div>
        </div>
      </IonContent>
    </IonPage>
  );
};

export default Register;
