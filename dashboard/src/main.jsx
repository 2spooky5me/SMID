import React from 'react'
import ReactDOM from 'react-dom/client'
import App from '/src/App'
import '/src/styles/index.css'
import { Provider } from 'react-redux';
import { store } from './redux/Store';

import { PersistGate } from 'redux-persist/integration/react';
import { persistStore } from 'redux-persist';

const persistor = persistStore(store);

ReactDOM.createRoot(document.getElementById('root')).render(
  <PersistGate persistor={persistor}>
    <Provider store={store}>
      <React.StrictMode>
        <App />
      </React.StrictMode>
    </Provider>
  </PersistGate>,
);