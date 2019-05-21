<?php

namespace App;

use Illuminate\Database\Eloquent\Model;
use Jenssegers\Mongodb\Eloquent\Model as Eloquent;

class Travel extends Eloquent
{
	protected $collection = 'travels';
}
