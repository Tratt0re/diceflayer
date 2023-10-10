import { HashRouter, Routes, Route } from "react-router-dom";
import { WebAppProvider, useExpand } from '@vkruglikov/react-telegram-web-app';
import useMountEffect from './utils/useMountEffect';
import RollResults from "./pages/RollResults";
import { DiceProvider } from "./contexts/DiceContext";
import DicesSelector from "./pages/DicesSelector";

function App() {
  // Initialize the useExpand hook to control the Telegram web app expansion
  const [isExpanded, expand] = useExpand();

  // Function to expand the Telegram web app when it starts
  const expandAtStart = () => {
    if (!isExpanded) {
      expand();
    }
  }

  // Use the useMountEffect hook to expand the app when it mounts
  useMountEffect(() => {
    expandAtStart();
  })

  // Render the application
  return (
    <WebAppProvider> {/* Provides context for the Telegram web app */}
      <DiceProvider> {/* Provides context for dice-related data */}
        <HashRouter> {/* Sets up routing using HashRouter */}
          <Routes> {/* Defines the routes for the application */}
            {/* Define a route for the DicesSelector component */}
            <Route path={`/`} element={<DicesSelector />} />
            {/* Define a route for the RollResults component */}
            <Route path={`/results`} element={<RollResults />} />
          </Routes>
        </HashRouter>
      </DiceProvider>
    </WebAppProvider>
  );
}

export default App;