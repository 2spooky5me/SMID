import { configureStore } from '@reduxjs/toolkit';
// Reducers made
import userReducer from './reducers/UserSlicer';
// persistor
import storage from 'redux-persist/lib/storage';
import { persistReducer } from 'redux-persist';
import { combineReducers } from '@reduxjs/toolkit';
import thunk from 'redux-thunk';

const persistConfig = {
	key: 'root',
	storage: storage,
	whitelist: ['userState'],
};

const rootReducer = combineReducers({
	userState: userReducer,

});

const persistedReducer = persistReducer(persistConfig, rootReducer);

export const store = configureStore({
	reducer: persistedReducer,
	middleware: [thunk],
});
