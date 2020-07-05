// Author: Fabio Pesari
// SPDX-License-Identifier: AGPL-3.0-or-later

function fetch_array(database, field) {
  return database['properties'][field]['items']['enum'];
}

function load_options(options, id) {
  let target = document.getElementById(id);
  options.forEach(function (option) {
      let element = document.createElement('option');
      element.innerHTML = option;
      target.appendChild(element);
  });
}

window.onload = function() {
  const arrays = ['licenses', 'formats', 'categories', 'repositories'];

  arrays.forEach(function (item) {
    load_options(fetch_array(database, item[0].toUpperCase() + item.slice(1)),
                 item);
  });

  const select_options = {
    search: true,
    descriptions: true,
    hideSelected: true,
    hideDisabled: true,
    multiLimit: -1,
    multiShowCount: false,
    width: '100%'
  };

  arrays.forEach(function (item){
    tail.select('#select-' + item, Object.assign(select_options,
    {multiContainer: '#mc-' + item}));
  });
}
