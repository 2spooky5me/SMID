import axios, { AxiosResponse } from 'axios';
import 'dayjs/locale/es';
import { isDayjs } from 'dayjs';

export const AxiosInstance = axios.create({
	baseURL: import.meta.env.VITE_APP_API_URL,
	headers: { 'Content-Type': 'application/json' },
	timeout: 10000,
});

export const mainUrls: GenericMethodType = {
	ASEGURADORAS:'contratantes/aseguradora',
	CONTRATANTES:'contratantes/contratante',
	AFILIADOS:'afiliados/afiliado',
	PLANES:'planes/plan',
	MEDICOS:'medicos/medico',
	SERVICIOS:'servicios/servicio',
	BAREMOS:'baremos/baremo',
	TASAS:'baremos/tasas',
	VALES:'vales/vale',
};
export const mainUrlsReports: GenericMethodType = {
	ASEGURADORAS:'contratantes/aseguradora/reporte',
	CONTRATANTES:'contratantes/contratante/reporte',
	AFILIADOS:'afiliados/afiliado/reporte',
	PLANES:'planes/plan/reporte',
	MEDICOS:'medicos/medico/reporte',
	SERVICIOS:'servicios/servicio/reporte',
	BAREMOS:'baremos/baremo/reporte',
	TASAS:'baremos/tasas/reporte',
	VALES:'vales/vale/reporte',
};
export const actionTitle: GenericMethodType = {
	PATCH: 'Modificar',
	POST: 'Guardar',
	DELETE: 'Eliminar',
	PRINT: 'Imprimir',
};
export const actionColor: GenericMethodType = {
	PATCH: 'warning',
	POST: 'success',
	DELETE: 'error',
	PRINT: 'info',
};

const ERROR_500 = {
	data: { 500: 'Error en el servidor, llamar al 2434' },
	status: 500
}

export const genericButtonsProps = {
	PATCH: { color: actionColor.PATCH },
	POST: { color: actionColor.POST },
	DELETE: { color: actionColor.DELETE },
	PRINT: {
		color: actionColor.PRINT,
		sx: {
			// Establecer el estilo para ocultar el botón en la impresión
			'@media print': {
				display: 'none',
			},
		},
	},
};

export const genericModalsAxiosMethods = {
	THEN:
		(
			setOpenModal: Function,
			clearValues: Function,
			notify: Function = (txt: string) => {},
			func: Function = (data: object) => {}
		) =>
		(response: AxiosResponse) => {
			setOpenModal(false);
			clearValues();
			if (response.data?.message) {
				notify(response.data.message || '¡Operación exitosa!');
			}
			// si se quiere añadir algo más
			func(response);
		},
	CATCH:
		(setErrorMsg = (t: string) => {}) =>
		(error: ResponseCustomType) => {
			//* Función para escribir el mensaje de error
			// Procesa los datos de los ERRORES predecibles
			// por ejemplo {identification: 'ide repetida'}
			// la convierte en texto para el mensaje

			let msg = Object.entries(error.data).map(([key, value]) => {
				if (!Array.isArray(value) && typeof value === 'object') {
					//* Ocurre si el value es un Object No array
					//* función recursiva, se llama a sí misma en este caso
					value = genericModalsAxiosMethods.CATCH()({ data: value });
				}
				return `[${key}: ${value}]\n`;
			});
			setErrorMsg(`Ha ocurrido un error: ${msg}`);
			return msg;
		},
};

export const actionsModalButtons = {
	PATCH:
		(values: AnyObj, initialValues: AnyObj, excludedKey = '') =>
		() => {
			const modifiedValues = Object.entries(values) // entries para iterar el values
				.filter(([key, value]) => initialValues[key] != value) // filtra los campos que se cambiaron
				.reduce((obj, [key, value]) => {
					/*
          Lo convierte en un diccionario los campos filtrados 
          key: La llave del campo filtrado, value: su valor
          obj: un diccionario que será reescrito para estructurarlo bien
          *{
          *  first_name: str
          *  birth_date: Dayjs
          *  ForeignRelated: value.id
          *}
          en la linea de abajo, hay una ternaria, donde verifica si el valor es un
          Dayjs, si es, entonces le pone el formato Str, si no, entonces
          verifica si tiene una propiedad de id, si no tiene entonces devuelve el value normal
          el obj se construirá en base a [key]:value
          al principio obj es un objeto vacío
          */
					if (key !== excludedKey) {
						value = isDayjs(value)
							? value.format('YYYY-MM-DD')
							: value?.id || value;
					}
					obj[key] = value;
					return obj;
				}, {});

			return modifiedValues;
		},
};

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
				navigate('/auth/logout/')
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
