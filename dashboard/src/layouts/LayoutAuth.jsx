import { Outlet } from 'react-router-dom';

const LayoutAuth = () => {
	return (
		<div className='fondo-login-auth print:bg-white'>
			<Outlet />
		</div>
	);
};

export default LayoutAuth;
