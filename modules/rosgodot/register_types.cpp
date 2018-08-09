#include "register_types.h"
#include "class_db.h"
#include "rosgodot.h"

void register_rosgodot_types() {

        ClassDB::register_class<RosGodot>();
}

void unregister_rosgodot_types() {
   //nothing to do here
}
