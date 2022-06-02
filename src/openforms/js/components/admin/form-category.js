import jsonScriptToVar from '../../utils/json-script';
import {apiCall} from '../../utils/fetch';

const init = () => {
  const nodes = document.querySelectorAll('.form-category');
  if (!nodes.length) return;
  // read the original GET params so we can include them in the async calls
  const GETParams = jsonScriptToVar('request-GET');
  nodes.forEach(node => loadFormsForCategory(node, GETParams));
};

const loadFormsForCategory = async (node, GETParams) => {
  const targetNode = node.querySelector('.form-category__form-list');
  const {id} = node.dataset;
  const query = new URLSearchParams({
    ...GETParams,
    _async: 1,
    category: id,
  });
  // TODO: handle pagination
  const response = await apiCall(`.?${query}`);
  const htmlBlob = await response.text();
  targetNode.innerHTML = htmlBlob;
};

document.addEventListener('DOMContentLoaded', () => {
  init();
});
