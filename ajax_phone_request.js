var settings = {
  "url": "https://api.ouedkniss.com/graphql",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "authority": "api.ouedkniss.com",
    "accept": "*/*",
    "accept-language": "en",
    "authorization": "",
    "content-type": "application/json",
    "dnt": "1",
    "locale": "en",
    "origin": "https://www.ouedkniss.com",
    "referer": "https://www.ouedkniss.com/",
    "save-data": "on",
    "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Microsoft Edge\";v=\"114\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67",
    "x-app-version": "\"2.1.28\""
  },
  "data": JSON.stringify({
    query: "query UnhidePhone($id: ID!) {\n  phones: announcementPhoneGet(id: $id) {\n    id\n    phone\n    phoneExt\n    hasViber\n    hasWhatsapp\n    hasTelegram\n    __typename\n  }\n}\n",
    variables: {"id":"36859965"}
  })
};

$.ajax(settings).done(function (response) {
  console.log(response);
});