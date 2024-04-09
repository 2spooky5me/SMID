import { createSlice } from '@reduxjs/toolkit';

const initialState = {
	accessToken: '',
	refreshToken: '',
	user: {
		username: 'Anónimo',
		email: '',
		first_name: '',
		last_name: '',
		is_superuser: false,
		is_staff: false,
		user_permissions: [],
	},
};

const userSlice = createSlice({
	name: 'user',
	initialState: initialState,

	reducers: {
		setUser: (state, action) => {
			state.accessToken = action.payload.token;
			state.refreshToken = action.payload['refresh-token'];
			state.user.username = action.payload.user.username;
			state.user.email = action.payload.user.email;
			state.user.first_name = action.payload.user.first_name;
			state.user.last_name = action.payload.user.last_name;
			state.user.is_superuser = action.payload.user.is_superuser;
			state.user.user_permissions = action.payload.user.user_permissions;
			state.user.is_staff = action.payload.user.is_staff;
		},
		unSetUser: state => {
			state.accessToken = '';
			state.refreshToken = '';
			state.user = {
				username: 'Anónimo',
				email: '',
				first_name: '',
				last_name: '',
				is_superuser: false,
				is_staff: false,
				user_permissions: [],
			};
		},
		setTokens: (state, action) => {
			state.accessToken = action.payload.access;
			state.refreshToken = action.payload.refresh;
		},
	},
	// construir los actions
});

export const { setUser, unSetUser, setTokens } = userSlice.actions;

export const accessTokenSelector = state => state.userState.accessToken;
export const refreshTokenSelector = state => state.userState.refreshToken;
export const usernameSelector = state => state.userState.user.username;
export const permissionsSelector = state => state.userState.user.user_permissions;
export const isStaffSelector = state => state.userState.user.is_staff;

export default userSlice.reducer;
