import axios, { AxiosResponse } from 'axios';
import 'dayjs/locale/es';
import { isDayjs } from 'dayjs';

export const AxiosInstance = axios.create({
	baseURL: import.meta.env.VITE_APP_API_URL,
	headers: { 'Content-Type': 'application/json' },
	timeout: 10000,
});


// an Axios object that can make GET and POST request more comfortable
export const axiosRequest = {
	HEADERS: (access: string) => {
		return {
			Authorization: `Bearer ${access}`,
			'Content-Type': 'application/json',
		};
	},
	GET: (url: string, access: string) => {
		return AxiosInstance.get(url, {
			headers: { ...axiosRequest.HEADERS(access) },
		});
	},

	POST: (url: string, access: string, body: object = {}) => {
		return AxiosInstance.post(
			url,
			{ ...body },
			{
				headers: { ...axiosRequest.HEADERS(access) },
			}
		);
	},
	PATCH: (url: string, access: string, body: object = {}) => {
		return AxiosInstance.patch(
			url,
			{ ...body },
			{
				headers: { ...axiosRequest.HEADERS(access) },
			}
		);
	},
	PUT: (url: string, access: string, body: object = {}) => {
		return AxiosInstance['put'](
			url,
			{ ...body },
			{ headers: { ...axiosRequest.HEADERS(access) } }
		);
	},
	DELETE: (url: string, access: string) => {
		return AxiosInstance['delete'](url, {
			headers: { ...axiosRequest.HEADERS(access) },
		});
	},
	// if I receive the instance of useDispatch() or another hook
	//i can use them in a outside functions
	REFRESH: async (
		refresh: string,
		dispatch: Function,
		setTokens: Function,
		navigate: Function
	) => {
		return AxiosInstance.post('api/token/refresh/', { refresh }).then(
			response => dispatch(setTokens(response.data))
		)
		.catch(error => {
			if(error?.response?.status === 401){
				navigate('/auth')
			}
		});
	},
	VERIFY: async (
		access: string,
		refresh: string,
		dispatch: Function,
		setTokens: Function,
		navigate: Function
	) => {
		return AxiosInstance.post(
			'api/token/verify/',
			{ token: access },
			{ headers: { 'Content-Type': 'application/json' } }
		).catch(error => {
			if (error?.response?.status === 401) {
				axiosRequest.REFRESH(refresh, dispatch, setTokens, navigate);
			} 
			// else { //! Comentado para que sólo el refresh reviente xd para q la gente no joda de q se le cierra por peticiones canceladas
			// 	navigate('/auth/logout/');
			// }
		});
	},
	POST_WITH_REFRESH: async (
		url: string,
		accessToken: string,
		refreshToken: string,
		dispatch: Function,
		setTokens: Function,
		navigate: Function,
		body: object
	) => {
		return await axiosRequest.POST(url, accessToken, body).catch(error => {
			if (!error?.response) {
				throw {
					data: { 500: 'Error en el servidor, llamar al 2434' },
					status: 500
				};
			} else if (error.response.status === 401) {
				axiosRequest.REFRESH(refreshToken, dispatch, setTokens, navigate);
			} else {
				throw error.response;
			}
		});
	},
	PATCH_WITH_REFRESH: async (
		url: string,
		accessToken: string,
		refreshToken: string,
		dispatch: Function,
		setTokens: Function,
		navigate: Function,
		body: AnyObj
	) => {
		return axiosRequest.PATCH(url, accessToken, body).catch(error => {
			if (!error?.response) {
				throw {
					data: { 500: 'Error en el servidor, llamar al 2434' },
				};
			} else if (error.response.status === 401) {
				axiosRequest.REFRESH(refreshToken, dispatch, setTokens, navigate);
			} else {
				throw error.response;
			}
		});
	},
	GET_WITH_REFRESH: async (
		url: string,
		accessToken: string,
		refreshToken: string,
		dispatch: Function,
		setTokens: Function,
		navigate: Function
	) => {
		return axiosRequest.GET(url, accessToken).catch(error => {
			if (!error?.response) {
				throw {
					data: { 500: 'Error en el servidor, llamar al 2434' },
				};
			} else if (error.response.status === 401) {
				axiosRequest.REFRESH(refreshToken, dispatch, setTokens, navigate);
			} else {
				throw error.response;
			}
		});
	},
	PUT_WITH_REFRESH: async (
		url: string,
		accessToken: string,
		refreshToken: string,
		dispatch: Function,
		setTokens: Function,
		navigate: Function,
		body: AnyObj
	) => {
		return axiosRequest.PUT(url, accessToken, body).catch(error => {
			if (!error?.response) {
				throw {
					data: { 500: 'Error en el servidor, llamar al 2434' },
				};
			} else if (error.response.status === 401) {
				axiosRequest.REFRESH(refreshToken, dispatch, setTokens, navigate);
			} else {
				throw error.response;
			}
		});
	},
	DELETE_WITH_REFRESH: async (
		url: string,
		accessToken: string,
		refreshToken: string,
		dispatch: Function,
		setTokens: Function,
		navigate: Function
	) => {
		return axiosRequest.DELETE(url, accessToken).catch(error => {
			if (!error?.response) {
				throw {
					data: { 500: 'Error en el servidor, llamar al 2434' },
				};
			} else if (error.response.status === 401) {
				axiosRequest.REFRESH(refreshToken, dispatch, setTokens, navigate);
			} else {
				throw error.response;
			}
		});
	},
};
