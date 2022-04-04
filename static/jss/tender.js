var tender_arr = new Array("Public","Private");

var cat_a = new Array();
cat_a[0]=""
cat_a[1]="Not currently available"
cat_a[2]="Educational Institutes|Office Complex|Entertainment|Housing|Hotels"

function populateTender(tenderElementId, categoryElementId)
{
	var tenderElement = document.getElementById(tenderElementId);
	tenderElement.length=0;
	tenderElement.options[0] = new Option('Choose Tender Type','-1');
	tenderElement.selectedIndex = 0;
	for (var i=0; i<tender_arr.length; i++) 
	{
		tenderElement.options[tenderElement.length] = new Option(tender_arr[i],tender_arr[i]);
	}

	if( categoryElementId )
	{
		tenderElement.onchange = function()
		{
			populateCategory( tenderElementId, categoryElementId );
		};
	}
}

function populateCategory( tenderElementId, categoryElementId )
{
	var selectedTenderIndex = document.getElementById( tenderElementId ).selectedIndex;

	var categoryElement = document.getElementById( categoryElementId );
	
	categoryElement.length=0;
	categoryElement.options[0] = new Option('Select Tender Category','');
	categoryElement.selectedIndex = 0;
	
	var category_arr = cat_a[selectedTenderIndex].split("|");
	
	for (var i=0; i<category_arr.length; i++) 
	{
		categoryElement.options[categoryElement.length] = new Option(category_arr[i],category_arr[i]);
	}
}