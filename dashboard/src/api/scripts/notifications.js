import { toast } from 'react-toastify';

export const notify = {
	CONFIG: {
		position: 'bottom-center',
		autoClose: 5000,
		hideProgressBar: false,
		closeOnClick: true,
		pauseOnHover: true,
		draggable: true,
		progress: undefined,
		theme: 'colored',
	},
	ERROR: texto => toast.error(texto, notify.CONFIG),
	SUCCESS: texto => toast.success(texto, notify.CONFIG),
	WARNING: texto => toast.warning(texto, notify.CONFIG),
	INFO: texto => toast.info(texto, notify.CONFIG),
};
