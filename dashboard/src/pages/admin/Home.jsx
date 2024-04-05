//? COMPONENTS
import Carnet from '/src/components/Carnet'
//? HOOKS
import { useEffect } from 'react';


export const Home = () => {

	// const navigate = useNavigate();
	// //* Redux global States
	// const token = useSelector(accessTokenSelector);
	// const refresh = useSelector(refreshTokenSelector);
	// const dispatch = useDispatch();

	// useEffect(() => {
	// 	axiosRequest.VERIFY(token, refresh, dispatch, setTokens, navigate)
	// }, []);

	return (
		<>
			<div className='flex items-center justify-center min-h-screen gap-12 '>
				<div className='bg-red-500 h-[60vh] w-[60vh] print:hidden'>
				</div>
				<Carnet />
			</div>
		</>
	);
};

export default Home;
