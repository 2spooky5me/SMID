// File to export validations with regex

// verify if a string is a phoneNumber 04141431755 while wirtting
export const isPhoneNumberWritting = (num:string):boolean => /^[0-9]{0,11}$/.test(num);
// verify if some string is a exact phoneNumber
export const isValidPhoneNumber = (num:string):boolean => /^0[24][124][1-69][0-9]{7}$/.test(num);
// verify if it's a valid rif number 2963522266 while writting
export const isRifWritting = (num:string):boolean => /^[0-9]{0,9}$/.test(num);
export const isValidRif = (num:string):boolean => /^[0-9]{6,10}$/.test(num);

export const isValidName = (text:string):boolean => /^[a-zá-źñ\s]{0,20}$/i.test(text);
//verify if it's a valid email like: leandrofermin@gmail.com or is
export const isValidEmail = (text:string):boolean =>
	/(^[a-z-_.0-9]+@[a-z]+\.[a-z]{2,4}(\.[a-z]{2,3})?$)|^$/i.test(text);

export const isValidFicha = (text:string):boolean => /^[0-9]{4}$/.test(text);

export const genericFormValidator =
	(setValues:Function, validator = (text:string) => true) =>
	(e:any) => {
		const { value, name } = e.target;
		if (validator(value)) {
			setValues((values:object) => ({ ...values, [name]: value }));
		}
	};

const regexValidation = {
	PHONE_NUMBER_W: isPhoneNumberWritting,
	VALID_PHONE_NUMBER: isValidPhoneNumber,
	RIF_W: isRifWritting,
	VALID_RIF: isValidRif,
	VALID_NAME: isValidName,
	VALID_EMAIL: isValidEmail,
};
export default regexValidation;
