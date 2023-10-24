/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Body_login_for_access_token_auth_token_post } from '../models/Body_login_for_access_token_auth_token_post';
import type { PostTrackResponse } from '../models/PostTrackResponse';
import type { TokenResponse } from '../models/TokenResponse';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class DefaultService {

    /**
     * Read Users Me
     * @returns any Successful Response
     * @throws ApiError
     */
    public static readUsersMeUserMeGet(): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/user/me',
        });
    }

    /**
     * Register User
     * @param email 
     * @param password 
     * @param firstName 
     * @param lastName 
     * @param pairingToken 
     * @returns any Successful Response
     * @throws ApiError
     */
    public static registerUserUserRegisterPost(
email: string,
password: string,
firstName: string,
lastName: string,
pairingToken?: string,
): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/user/register',
            query: {
                'email': email,
                'password': password,
                'first_name': firstName,
                'last_name': lastName,
                'pairing_token': pairingToken,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Post Stampinout
     * @returns PostTrackResponse Successful Response
     * @throws ApiError
     */
    public static postStampinoutLogStampinoutPost(): CancelablePromise<PostTrackResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/log/stampinout',
        });
    }

    /**
     * Get Stats
     * @returns any Successful Response
     * @throws ApiError
     */
    public static getStatsLogStatsGet(): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/log/stats',
        });
    }

    /**
     * Login For Access Token
     * @param formData 
     * @returns TokenResponse Successful Response
     * @throws ApiError
     */
    public static loginForAccessTokenAuthTokenPost(
formData: Body_login_for_access_token_auth_token_post,
): CancelablePromise<TokenResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/auth/token',
            formData: formData,
            mediaType: 'application/x-www-form-urlencoded',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Get Pairing Token
     * @param sn 
     * @returns any Successful Response
     * @throws ApiError
     */
    public static getPairingTokenChipPairingTokenGet(
sn: number,
): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/chip/pairing-token',
            query: {
                'sn': sn,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Claim Pairing Token
     * @param pairingToken 
     * @returns any Successful Response
     * @throws ApiError
     */
    public static claimPairingTokenChipPairingTokenPost(
pairingToken: string,
): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/chip/pairing-token',
            query: {
                'pairing_token': pairingToken,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Root
     * @returns any Successful Response
     * @throws ApiError
     */
    public static rootGet(): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/',
        });
    }

}
