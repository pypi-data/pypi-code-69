import aurorax as _aurorax
import datetime as _datetime
from typing import Dict as _Dict


def ephemeris(start_dt: _datetime, end_dt: _datetime, program: str = None, platform: str = None,
              instrument_type: str = None, source_type: str = None, owner: str = None,
              format: str = "basic_info") -> _Dict:
    """
    Retrieve information about the number of existing ephemeris records

    :param start_dt: start date
    :type start_dt: datetime
    :param end_dt: end date
    :type end_dt: datetime
    :param program: program name to filter sources by, defaults to None
    :type program: str, optional
    :param platform: platform name to filter sources by, defaults to None
    :type platform: str, optional
    :param instrument_type: instrument type to filter sources by, defaults to None
    :type instrument_type: str, optional
    :param source_type: source type to filter sources by (heo, leo, lunar, or ground), defaults to None
    :type source_type: str, optional
    :param owner: owner ID to filter sources by, defaults to None
    :type owner: str, optional
    :param format: the format of the ephemeris source returned (identifier_only, basic_info,
                   full_record), defaults to "basic_info"
    :type format: str, optional

    :return: ephemeris availability information
    :rtype: Dict
    """
    params = {
        "start": start_dt.strftime("%Y-%m-%d"),
        "end": end_dt.strftime("%Y-%m-%d"),
        "program": program,
        "platform": platform,
        "instrument_type": instrument_type,
        "source_type": source_type,
        "owner": owner,
        "format": format,
    }
    req = _aurorax.AuroraXRequest(_aurorax.api.URL_EPHEMERIS_AVAILABILITY, params=params)
    res = req.execute()
    return_dict = {
        "status_code": res.status_code,
        "data": res.data
    }
    return return_dict


def data_products(start_dt: _datetime, end_dt: _datetime, program: str = None, platform: str = None,
                  instrument_type: str = None, source_type: str = None, owner: str = None,
                  format: str = "basic_info") -> _Dict:
    """
    Retrieve information about the number of existing data product records

    :param start_dt: start date
    :type start_dt: datetime
    :param end_dt: end date
    :type end_dt: datetime
    :param program: program name to filter sources by, defaults to None
    :type program: str, optional
    :param platform: platform name to filter sources by, defaults to None
    :type platform: str, optional
    :param instrument_type: instrument type to filter sources by, defaults to None
    :type instrument_type: str, optional
    :param source_type: source type to filter sources by (heo, leo, lunar, or ground), defaults to None
    :type source_type: str, optional
    :param owner: owner ID to filter sources by, defaults to None
    :type owner: str, optional
    :param format: the format of the ephemeris source returned (identifier_only, basic_info,
                   full_record), defaults to "basic_info"
    :type format: str, optional

    :return: ephemeris data product information
    :rtype: Dict
    """
    params = {
        "start": start_dt.strftime("%Y-%m-%d"),
        "end": end_dt.strftime("%Y-%m-%d"),
        "program": program,
        "platform": platform,
        "instrument_type": instrument_type,
        "source_type": source_type,
        "owner": owner,
        "format": format,
    }
    req = _aurorax.AuroraXRequest(_aurorax.api.URL_DATA_PRODUCTS_AVAILABILITY, params=params)
    res = req.execute()
    return_dict = {
        "status_code": res.status_code,
        "data": res.data
    }
    return return_dict
