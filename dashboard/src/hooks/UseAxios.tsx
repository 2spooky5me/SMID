import { useDispatch, useSelector } from "react-redux";
import { axiosRequest } from "../api/axios";
import { accessTokenSelector, refreshTokenSelector, setTokens } from "../redux/reducers/UserSlicer";
import { useNavigate } from "react-router-dom";
import { AxiosResponse } from "axios";


function useAxios(){
  const dispatch = useDispatch();
	const access = useSelector(accessTokenSelector);
	const refresh = useSelector(refreshTokenSelector);
  const navigate = useNavigate();
  
  const requestHandler = (method:string, endpoint:string, body?:Object):Promise<AxiosResponse<any, any>> => {
    return axiosRequest[`${method.toUpperCase()}_WITH_REFRESH`](
      endpoint,
      access,
			refresh,
			dispatch,
			setTokens,
			navigate,
			body,
    )
  }
  
  return requestHandler;
}

export default useAxios;